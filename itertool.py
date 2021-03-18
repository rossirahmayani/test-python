import itertools
import operator

a = [1,2,3]
b = [4]

# product
prod = itertools.product(a,b, repeat=2)
print(list(prod))

# permutation
permut = itertools.permutations(a)
print(list(permut))

# combination
comb = itertools.combinations(a,2)
print(list(comb))

comb_repl = itertools.combinations_with_replacement(a,2)
print(list(comb_repl))

#accumulate
acc = itertools.accumulate(a)
print(a)
print(list(acc))

acm = itertools.accumulate(a, func=operator.mul)
print(list(acm))

# groupby
def odd(x):
    return x % 2 == 1

group = itertools.groupby(a, key=odd)
for key, value in group:
    print(key, list(value))

# count
for i in itertools.count(10):
    print(i)
    if i == 16:
        break

# cycle
count = 0
for i in itertools.cycle(a):
    print(i)
    if i == 3:
        count = count + 1
    if count == 3:
        break


# repeat
for i in itertools.repeat(10, 5):
    print(i)