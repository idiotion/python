# -*- coding: utf-8 -*-

# def log(func):
#     def aaaa(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return aaaa

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# import functools
# 
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

import functools

def log(arg):
        
    def decorator(func=arg):
        text='call' if func==arg else arg
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():' % (text,func.__name__)
            func(*args, **kw)
            print 'end %s %s():' % (text, func.__name__)
            #return res
        return wrapper
    
    return decorator() if callable(arg) else decorator

@log
def now():
    print '2015-3-25'
    
# print type(now)
f=now
#print type(f)
f()
   
# print now.__name__
# print f.__name__