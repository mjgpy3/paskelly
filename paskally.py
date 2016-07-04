identity = lambda x: x
identity.sign = ['a', 'a']
identity.example = lambda: identity(42) == 42

const = lambda x: lambda _: x
const.sign = ['a', 'b', 'a']
const.example = lambda: const(42)(99) == 42

if __name__ == '__main__':
  units = [
    identity,
    const
  ]
  for fn in units:
    assert fn.example()
