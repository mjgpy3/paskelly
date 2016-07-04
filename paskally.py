num = lambda name: 'Num ' + name
lizst = lambda inner: 'List ' + inner

def curry_n(n, fn, args = []):
  if n - len(args) == 0:
    return fn(*args)
  return lambda *args2: curry_n(n, fn, args + list(args2))

curry_n.sign = ['int', ['(a, ..., m)', 'n'], ['a', '...', 'm', 'n']]
curry_n.example = lambda: curry_n(3, lambda a, b, c: a + b * c)(1, 2)(3) == 7

identity = lambda x: x
identity.sign = ['a', 'a']
identity.example = lambda: identity(42) == 42

const = curry_n(2, lambda a, _: a)
const.sign = ['a', 'b', 'a']
const.example = lambda: const(42)(99) == 42

def do_foldr(fn, init, values):
  if len(values) == 0:
    return init
  return fn(values[0], do_foldr(fn, init, values[1:]))

foldr = curry_n(3, do_foldr)
foldr.sign = [['a', 'b', 'b'], 'b', lizst('a'), 'b']
foldr.example = lambda: foldr(lambda a, b: a - b, 0, [1, 2, 3]) == 2

compose2 = curry_n(3, lambda f, g, x: f(g(x)))
compose2.sign = [['b', 'c'], ['a', 'b'], ['a', 'c']]
compose2.example = lambda: compose2(lambda a: a * 2, lambda a: a + 1)(20) == 42

compose = lambda *args: foldr(compose2, identity, args)
compose.example = lambda: compose(
  lambda a: a * 2,
  lambda a: a + 1,
  lambda a: 4 * a
  )(5) == 42

reverse_fn = lambda fn: lambda *args: fn(*args[::-1])
reverse_fn.example = lambda: reverse_fn(lambda a, b: a - b)(2, 44) == 42

pipe = reverse_fn(compose)
pipe.example = lambda: pipe(
  lambda a: 4 * a,
  lambda a: a + 1,
  lambda a: a * 2
  )(5) == 42

nth_arg = lambda n: lambda *args: args[n]
nth_arg.sign = ['int', '(a, .., m)', 'a|...|m']
nth_arg.example = lambda: nth_arg(2)(1, 2, 42, 4) == 42

of = lambda x: [x]
of.sign = ['a', lizst('a')]
of.example = lambda: of(42) == [42]

add = curry_n(2, lambda a, b: a + b)
add.sign = [num('a'), num('a'), num('a')]
add.example = lambda: add(1)(41) == 42

multiply = curry_n(2, lambda a, b: a * b)
multiply.sign = [num('a'), num('a'), num('a')]
multiply.example = lambda: multiply(21)(2) == 42

inc = add(1)
inc.sign = [num('a'), num('a')]
inc.example = lambda: inc(41) == 42

dec = add(-1)
dec.sign = [num('a'), num('a')]
dec.example = lambda: dec(43) == 42

equals = curry_n(2, lambda a, b: a == b)
equals.sign = ['a', 'a', 'bool']
equals.example = lambda: equals(42)(42)

if_else = curry_n(4, lambda p, c, a, v: c(v) if p(v) else a(v))
if_else.sign = [['a', 'bool'], ['a', 'b'], ['a', 'b'], 'a', 'b']
if_else.example = lambda: if_else(equals(41), add(1), add(-1))(41) == 42

if __name__ == '__main__':
  units = [
    curry_n,
    compose2,
    compose,
    pipe,
    reverse_fn,
    foldr,
    identity,
    nth_arg,
    const,
    of,
    add,
    multiply,
    inc,
    dec,
    equals,
    if_else
  ]
  for fn in units:
    assert fn.example()
