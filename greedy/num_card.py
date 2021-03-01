# -*- coding: utf-8 -*-
n,m=map(int,input().split())
result=0
for i in range(n):
    li_=(list(map(int,input().split())))
    min_=min(li_)
    result=max(result,min_)
print(result)
