s=input()
count0=0 #0되는 값
count1=0 #1되는 값
#바뀔때마다 값 더하여 가장 작은값 찾기
if s[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        if s[i+1]=='1':
            count0+=1
        else:
            count1+=1
        
print(min(count0,count1))