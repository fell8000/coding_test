# -*- coding: utf-8 -*-

n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
#제일 큰 수 
count=(k*(m//(k+1))+m%(k+1))
ans=data[-1]*count
ans+=data[-2]*(m-count)

print(ans)
