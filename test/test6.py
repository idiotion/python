# -*- coding: utf-8 -*-

import time

def findchr(string,char):
    lenstring=len(string)
    lenchar=len(char)
    char.strip()
    string.strip()
    res=-1
    
    if lenstring < lenchar or lenstring == 0 or lenchar == 0:
        return -1
    
    for i in range(len(string)):
        splitstr=string[i:i+lenchar]
        if splitstr==char:
            res=i
            break
    
    return res

def riqi(argv):
    a = "2013-10-10 23:40:00"
    timeArray = time.strptime(argv, "%Y-%m-%d %H:%M:%S")
    print timeArray

if __name__ == '__main__':
    from sys import argv

    script, first, second, third= argv
    
    print "The script is called:", script
    print "Your first variable is:", first
    print "Your second variable is:", second
    print "Your third variable is:", third