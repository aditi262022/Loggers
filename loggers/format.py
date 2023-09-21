#Format logger example

import logging
logging.basicConfig(filename='log1.txt',level=logging.DEBUG,filemode='w',format='time=%(asctime)s,filename=%(filename)s,functionname=%(funcName)s')
def fun():
    try:
        a=int(input('enter the num1 \n'))
        logging.debug('a={}'.format(a))
        b=int(input('enter the num2 \n'))
        logging.debug('b={}'.format(b))
        return a/b
    except:
        print('Some problem occurred')

if __name__ == '__main__':
    print(fun())
