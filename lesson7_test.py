# -*- coding: utf-8 -*-

def tr(srcstr, dststr, string):
    
    if len(srcstr) != len(dststr):
        return
    
    if srcstr in string:
        resstr=string.replace(srcstr,dststr)
    else:
        resstr=dststr+string
    
    return resstr

if __name__ == '__main__':
    a=input('input srcstr:')
    b=input('input dststr:')
    c=input('input string:')
    d=tr(a, b, c)
    print(d)
    