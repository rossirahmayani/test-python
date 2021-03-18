
x = -5
y = 0

# raise
# if x < 0:
#     raise Exception('x should be positive')

# assert
# assert(x >= 0), 'x is not positive'

# try catxh
try:
    a = x / y
except Exception as e:
    print('Error: {}'.format(e))
else:
    print(a)
finally:
    print('DONE')