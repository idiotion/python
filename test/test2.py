# -*- coding: utf-8 -*-

import operator


def getinput():
    args=raw_input('输入待求值的数字，以逗号分隔：')
    inlist=args.split(',')
    retlist=[]
    for i in inlist:
        if i.lstrip() == '':
            continue
        elif i.isdigit():
            try:
                res=int(i)
            except ValueError:
                raise ValueError,'[ %s ]为非法的数字类型！' %(i)
        else:
            try:
                res=float(i)
            except ValueError:
                raise ValueError,'[ %s ]为非法的浮点数!' %(i)
            
        retlist.append(res)
    return retlist

def sums(inlist):
    return sum(inlist)

def avgs(inlist):
    return float(sum(inlist))/len(inlist)

CMDs={'S':sums,'A':avgs}

def main():
    while True:
        arg=raw_input('''请输入想执行的命令
        S: 得到数组的和
        A: 得到数据的平均值
        X: 退出
        ''').upper()
    
        if arg not in 'SAX':
            print '请重新输入！'        
            continue
        
        if arg == 'X':
            print '正常退出！'
            break
        
        inlist=getinput()
        ret=CMDs[arg](inlist)
        print ret
            
if __name__ == '__main__':
    main()