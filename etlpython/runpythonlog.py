#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os,functools,datetime,traceback,logging

'''
log process for all script support 2 mode
@log
@log(filename)
define env "LOGDIR" is best
'''

def log(arg):
    
    def decorator(func=arg):
        logdir=os.getenv('LOGDIR')
        logfilename='runpython.log' if func==arg else arg
        logfile=os.path.join(logdir,logfilename) if logdir is not None else logfilename
        
        @functools.wraps(func)
        def wrapper(*args,**kw):
            bgnstr=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            status='SUCC'
            err=''
            
            try:
                res=func(*args, **kw)
            except Exception:
                status='FAIL'
                err='|'+traceback.format_exc()
                raise
            finally:
                endstr=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                funcstr=func.__name__+(str(args) if len(args)>0 else '')+(str(kw) if len(kw)>0  else '')
                logstr=bgnstr+'|'+endstr+'|'+funcstr+'|'+status+err
                print logstr
                with open(logfile,'a') as f:
                    f.write(logstr+os.linesep)
            if err:
                raise
            return res
                    
        return wrapper
    return decorator() if callable(arg) else decorator

@log
def main(args):
    print 'log test succ'
    return 'test 1 succ'

@log('testpython.log')
def testlog(args):
    print 'log test2 succ'
    return 'test 2 succ'
    
if __name__ == '__main__':
    ss=main(sys.argv)
    print ss
    st=testlog(sys.argv)
    print st