# -*- coding: utf-8 -*-
import math
import functools

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    
def age18(x):
    if x >= 18:
        pass
    else:
        return '18岁以下不合法!'
    
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def quadratic(a, b, c):
    if not isinstance(a, (int)):
        raise TypeError('bad operand type for a')
    if not isinstance(b, (int)):
        raise TypeError('bad operand type for b')
    if not isinstance(c, (int)):
        raise TypeError('bad operand type for c')
    if a == 0:
        x=-c/b
    else:
        x=((-b + math.sqrt(b**2 - 4*a*c) )/(2*a),(-b - math.sqrt(b**2 - 4*a*c) )/(2*a))
    return x

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

def move(n,a,b,c):
    if n==1:
       print('%s --> %s' %(a,c))
    else:
       move(n-1,a,c,b)
       print('%s --> %s' %(a,c))
       move(n-1,b,a,c)
#    move(3, 'a', 'b', 'c')

def str2float(s):
    def fn(x,y):
        return x * 10 + y
    def chr2num(x):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x]
    npos=s.index('.')
#     p1=reduce(fn,map(chr2num,s[0:npos]))
#     p2=reduce(fn,map(chr2num,s[npos+1:]))/(10**(len(s)-npos-1))
#    return p1+p2
    return reduce(fn, map(chr2num,s.replace('.','')))/(10**(len(s)-npos-1))
 
#print('str2float(\'123.456\') =', str2float('123456.003'))

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator