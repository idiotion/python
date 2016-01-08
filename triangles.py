# -*- coding: utf-8 -*-

def triangles():
    L=[1]
    while True:
        yield L
        L.append(1)
        for i in range(len(L)-2,0,-1):
            L[i] += L[i-1]
            
n=0
for t in triangles():
    print(t)
    n=n+1
    if n==5:
        break