#Normal example

def fun():
    try:
        a=int(input('enter the num1 \n'))
        print(a)
        b=int(input('enter the num2 \n'))
        print(b)
        return a/b
    except:
        print('Some problem occurred')

if __name__ == '__main__':
    print(fun())
