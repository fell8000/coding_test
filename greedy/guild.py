n=map(int, input())
gongpo=list(map(int, input().split()))

gongpo.sort()
count=0
result=0

for i in gongpo:
    count+=1
    if count >= i:
        result+=1
        count=0
    
print(result)