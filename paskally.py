num = lambda name: 'Num ' + name

identity = lambda x: x
identity.sign = ['a', 'a']
identity.example = lambda: identity(42) == 42

const = lambda x: lambda _: x
const.sign = ['a', 'b', 'a']
const.example = lambda: const(42)(99) == 42

add = lambda a: lambda b: a + b
add.sign = [num('a'), num('a'), num('a')]
add.example = lambda: add(1)(41) == 42

equals = lambda a: lambda b: a == b
equals.sign = ['a', 'a', 'bool']
equals.example = lambda: equals(42)(42)

if_else = lambda p: lambda c: lambda a: lambda v: c(v) if p(v) else a(v)
if_else.sign = [['a', 'bool'], ['a', 'b'], ['a', 'b'], 'a', 'b']
if_else.example = lambda: if_else(equals(41))(add(1))(add(-1))(41) == 42

if __name__ == '__main__':
  units = [
    identity,
    const,
    add,
    equals,
    if_else
  ]
  for fn in units:
    assert fn.example()
