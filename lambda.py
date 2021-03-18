import functools

# penulisan --> lambda (param): isi method param
add10 = lambda x: x + 10
print(add10(2))

mul = lambda x,y: x*y
print(mul(3,4))

point2d = [(1,2), (2,4), (1,5), (3,6)]
point2d_sorted = sorted(point2d, key=lambda x: x[1])
print(point2d)
print(point2d_sorted)

# map
a = [1,2,3,4,5]
b = map(lambda x: x * 2, a) #map(lambda funct, sequence)
print(list(b))

# filter
c = filter(lambda x: x % 2 == 0, a) #isi fungsi harus return boolean
print(list(c))

# reduce
d = functools.reduce(lambda x,y: x*y, a)
print(d)