# -*- coding: utf-8 -*-


n,m,k=map(int,input().split())
data=list(map(int,input().split()))
data.sort()

result=((data[-1]*k+data[-2])*(m//(k+1)))+data[-1]*(m%(k+1))
print(result)