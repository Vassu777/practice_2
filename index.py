class operations():
    c=12
    def add(a,b):
        c=a+b
        print(c)
        print('im adding classes')
    add(2,4)

class operations2(operations):

    print(operations.c)
