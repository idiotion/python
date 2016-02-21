from time import time
from itertools import izip

adict={'a':1,'b':2}
bdict={'c':1,'d':2,'f':3,'e':2}

a=[1,2,3,4,5]
b=['a','b','c','d','e']
 
cdict=dict(zip(a,b))
print cdict

def resver(argv):
    print dict(izip(argv.itervalues(),argv.iterkeys()))

resver(cdict)
# print bdict.items()
#  
# cdict=sorted(bdict.items(),key=lambda v:v[0])
#   
# print cdict

# for i in sorted(bdict):
#     print i,bdict[i]

# def m1():
#     cdict=dict(adict,**bdict)
#     return cdict
# def m2():
#     cdict=dict(adict.items()+bdict.items())
#     return cdict
# def m3():
#     cdict=dict(adict)
#     cdict.update(bdict)
#     return cdict
# def m4():
#     cdict=adict.copy()
#     cdict.update(bdict)
#     return cdict
# bgnts=time()
# 
# for i in range(1,int(1e6)):
#     m1()
# 
# endts=time()
# 
# print endts-bgnts