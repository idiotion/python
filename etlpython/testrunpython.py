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
#raise AssertionError,'hahahahaha'