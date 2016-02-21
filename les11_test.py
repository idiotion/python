# -*- coding: utf-8 -*-

# def counter(start_at=0):
#     count = start_at
#     while True:
#         val = (yield count)
#         if val is not None:
#             count = val
#         else:
#             count += 1

class AddrBookEntry(object): # 类定义
    'address book entry class'
    foo=100
    def __init__(self, nm, ph): # 定义构造器
        self.name = nm # 设置 name
        self.phone = ph # 设置 phone
        print 'Created instance for:', self.name
        
    def updatePhone(self, newph): # 定义方法
        self.phone = newph
        print 'Updated phone# for:', self.name