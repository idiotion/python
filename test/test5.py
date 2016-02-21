# -*- coding: utf-8 -*-
import re

def muli(x,y):
    return x*y

def isrun(argv):
    a=argv%4
    b=argv%100
    if a==0 and b != 0:
        return True
    if a==0 and b==0:
        return True
    return False

def changemoney(dollar):
    centlist=[1,5,10,25]
    tarcent=int(dollar*100)
    if dollar>1:
        print '不用换!'
        return
    
    changelist=[]
    centlist.sort(reverse=True)
    
    i=0
    while i<len(centlist):
        a=divmod(tarcent,centlist[i])
        changelist.append(a[0])
        
        tarcent-=a[0]*centlist[i]
        i+=1
    return changelist

def compute(argv):
    srlist=['+','-','**','%','*']
    
    for i in srlist:
        a=argv.split(i)
        if len(a)==2 and i=='*':
            return muli(float(a[0]), float(a[1]))
            
def lilv(money,years):
    lv=0.03
    res=money*(1+lv)
    if years==1:
        return res
    else:
        return lilv(res, years-1)
    
def main():
#     x=input('请输入要兑换的零钱:')
#     change=changemoney(x)
#     print '%d 个25美分，%d 个10美分，%d 个5美分，%d 个1美分' % (change[0],change[1],change[2],change[3])
#     x=raw_input('请输入你的表达式:')
#     res=compute(x)
#     print res
    money=input('money:')
    years=input('years:')
    print lilv(money,years)
    
if __name__ == '__main__':
    main()