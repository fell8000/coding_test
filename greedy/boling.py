n,m=map(int,input().split())
k=list(map(int,input().split()))

k.sort()

result=0

for i in range(n-1):
    for j in range(i,n):
        if k[i]!=k[j]:
            result+=1
        
print(result)