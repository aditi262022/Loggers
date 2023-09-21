import logging
info_logger=logging.getLogger('info')
debug_logger=logging.getLogger('debug')
error_logger=logging.getLogger('error')

info_logger.setLevel(logging.INFO)
debug_logger.setLevel(logging.DEBUG)
error_logger.setLevel(logging.ERROR)

info_log=logging.FileHandler('infolog.txt')
debug_log=logging.FileHandler('debuglog.txt')
error_log=logging.FileHandler('errorlog.txt')

info_logger.addHandler(info_log)
debug_logger.addHandler(debug_log)
error_logger.addHandler(error_log)

'''
info_log.setFormatter('form')
debug_log.setFormatter('form')
error_log.setFormatter('form')
'''

def fun():
    try:
        info_logger.info('fun() is called..!')
        a=int(input('enter the num1 \n'))
        debug_logger.debug('a={}'.format(a))
        b=int(input('enter the num2 \n'))
        debug_logger.debug('b={}'.format(b))
        return a/b
    except:
        print('some problem occurred')
        info_logger.info('exception was handled.!')
        error_logger.exception('exception occurred as given below')

if __name__ == '__main__':
    info_logger.info('main() is called')
    res=fun()
    debug_logger.debug('res={}'.format(res))

