#INFO logger example

import logging
logging.basicConfig(filename='log.txt',level='logging.INFO',filemode='w')
def fun():
    try:
        logging.info('fun() is called..!')
        a=int(input('enter the num1 \n'))
        b=int(input('enter the num2 \n'))
        return a/b
    except:
        logging.info('exception is handled..!')
        print('Some problem occurred')

if __name__ == '__main__':
    logging.info('main() is called')
    print(fun())

'''
op 

enter the num1 
10
enter the num2 
0
Some problem occurred
None
'''
