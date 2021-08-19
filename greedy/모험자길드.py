# -*- coding: utf-8 -*-

n=map(int,input().split()) #사람수
data=list(map(int,input().split())) #공포도 1 2 2 2 3
data.sort()
result=0 #최대값
group=0
for d in data:
    group+=1
    if d<=group:
        group=0
        result+=1
print(result)

 