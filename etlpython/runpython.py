#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import runpylog

def cur_file_dir():
    path=sys.path[0]
    
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

@runpylog.runpylog
def main(args):
    curpath=cur_file_dir()
    if curpath:
        os.chdir(curpath)
    myproc=subprocess.Popen('python '+args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    ret=myproc.wait()
    if ret != 0:
        errmsg=myproc.stderr.read()
        raise IOError, errmsg
    print myproc.stdout.read()
    
if __name__ == '__main__':
    if not sys.argv or len(sys.argv)<=1:
        sys.exit()
         
    arg=' '.join(sys.argv[1:])
    main(arg)