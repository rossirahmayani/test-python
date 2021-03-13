def hello(name):
    return f'Hello {name}'


def total(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    return (*numbers, total)
