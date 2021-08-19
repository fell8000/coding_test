# -*- coding: utf-8 -*-

n,m=map(int,input().split())
result=0
for i in range(n):
    data=list(map(int,input().split()))
    minv=min(data)
    result=max(minv,result)
print(result)