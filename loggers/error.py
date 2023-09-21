#ERROR logger example

import logging
logging.basicConfig(filename='log2.txt',level=logging.ERROR)
def fun():
    try:
        a=int(input('enter the num1 \n'))
        b=int(input('enter the num2 \n'))
        return a/b
    except Exception as e:
        print('Some problem occurred')
        logging.error(e)

if __name__ == '__main__':
    print(fun())