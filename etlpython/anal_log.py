#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import subprocess

remotepath={'192.168.55.68':'/wls103/bea/ttserver'}

timeline=50
lcoaldir='/data11/ecif'

if len(sys.argv)<=1:
    sys.exit()

etldate=sys.argv[1]

if len(etldate)!=8:
    sys.exit()
    
logfilename='ttserver.log.%s-%s-%s' % (etldate[:4],etldate[4:6],etldate[6:8])
logpath='/data11/ecif/%s' % etldate

if not os.path.isdir(logpath):
    chkdir=subprocess.Popen('mkdir -p '+logpath,shell=True)
    chkdir.wait()
    
os.chdir(logpath)

regsec=re.compile(r'(\d)+ms')
regtime=re.compile(r'([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2}):([0-9]{2})')

def cpremotefile(remoteserverip,remotelogpath):
    localfilename='%s_%s' % (logfilename,remoteserverip)
    cmd='scp wls103@%s:%s/%s %s/%s' %(remoteserverip,remotelogpath,logfilename,
                                      logpath,localfilename)
    cpfile=subprocess.Popen(cmd,shell=True)
    cpres=cpfile.wait()
    if cpres != 0:
        raise
    return localfilename

def anallog(logfile):
    cnt=0
    errnum=0
    morethan50msnum=0
    secs=0
    
    try:
        f=open(logfile,'r')
        for line in f.readlines():
            reline=regsec.search(line)
            if reline:
                sec=int(reline.groups()[0])
                secs+=sec
                cnt+=1
                morethan50msnum+=1 if sec>timeline else 0
            else:
                if regtime.search(line):
                    errnum+=1
    except IOError:
        return
    finally:
        f.close()
    
    return (secs,cnt,morethan50msnum,errnum)
    
def insdata(arg):
    pass

if __name__=='__main__':
    for key,value in remotepath.items():
        locallogfile=cpremotefile(key,value)
        anallog(locallogfile)