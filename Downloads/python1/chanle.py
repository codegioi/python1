n=int(input())
arr=list(map(int,input().split()))
dem=0
count=0
sum1=0
tong=0
for x in arr:
    if x%2==0:
        dem+=1
        sum1=sum1+x
    else:
        count+=1
        tong=tong+x
print(dem)
print(count) 
print(sum1)
print(tong)
