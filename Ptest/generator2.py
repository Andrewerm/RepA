def gen_fun():
    print('block 1')
    yield 1
    print('block 2')
    yield 2
    print('end')

for i in gen_fun():
    print(i)