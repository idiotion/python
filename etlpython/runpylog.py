#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import functools
import traceback
import logging

'''
log process for all script support 2 mode
@log
@log(filename)
define env "LOGDIR" is best
'''

def runpylog(arg):
    def decorator(func=arg):
        logdir=os.getenv('LOGDIR')
        logfilename='runpython.log' if func==arg else arg
        logfile=os.path.join(logdir,logfilename) if logdir else logfilename
        
        @functools.wraps(func)
        def wrapper(*args,**kw):
            status='SUCC'
            err=''
            
            try:
                res=func(*args, **kw)
            except Exception:
                status='FAIL'
                err='|'+traceback.format_exc()
                raise
            finally:
                funcstr=(str(args) if len(args)>0 else '')+(str(kw) if len(kw)>0  else '')
                logstr=funcstr+'|'+status+err
                
                logformat='P%(process)d|%(asctime)s|%(relativeCreated)dms|%(message)s'
                logging.basicConfig(level=logging.DEBUG,
                                    format=logformat,
                                    datefmt='%Y-%m-%d %H:%M:%S',
                                    filename=logfile)
                console=logging.StreamHandler()
                console.setLevel(logging.DEBUG)
                console.setFormatter(logging.Formatter(logformat))
                logging.debug(logstr)
                logging.getLogger('').addHandler(console)
                
            return res
                    
        return wrapper
    return decorator() if callable(arg) else decorator

@runpylog
def main(args):
    print 'log test succ'
    return 'test 1 succ'

@runpylog('testpython.log')
def testlog(args):
    print 'log test2 succ'
    return 'test 2 succ'
    
if __name__ == '__main__':
    ss=main(sys.argv)
    print ss
    
    st=testlog(sys.argv)
    print st