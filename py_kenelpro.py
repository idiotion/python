# -*- coding: utf-8 -*-

def nn(num):
    res=1
    while num>1:
        res=res*num
        num-=1
    
    return res
    
def isprime(num):
    count=int(num/2)
    if num>0:
        while count > 1:
            if num%count==0:
                break
            else:
                count-=1
    
    if count == 1:
        return True
    else:
        return False
    
if __name__ == '__main__':
    print([x for x in range(100) if isprime(x)])