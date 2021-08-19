# -*- coding: utf-8 -*-

n,k=map(int,input().split())
result=0
while n>1:
    if n%k==0:
        n=n//k
        result+=1
    else:
        num=n%k
        result+=num
        n=n-num
print(result)