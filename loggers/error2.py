#ERROR logger example-2

import logging
logging.basicConfig(filename='log2.txt',level=logging.ERROR)
def fun():
    try:
        a=int(input('enter the num1 \n'))
        b=int(input('enter the num2 \n'))
        return a/b
    except:
        print('Some problem occurred')
        logging.exception('invalid inputs leading to problem')

if __name__ == '__main__':
    print(fun())