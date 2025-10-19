def tongchuso(n):
    sum=0
    while n!=0:
        temp=n%10
        sum+=temp
        n=n//10
    return sum
def rev(n):
    rev=n
    sum=0
    while n!=0:
        temp=n%10
        sum=sum*10+temp
        n=n//10
    if rev==sum:
        return True
    else:
        return False
def fibo(n):
    if n == 0:
        return True
    elif n == 1:
        return True
    else:
        fn1 = 0
        fn2 = 1 # fn1 = F1, fn2 = F0
        for i in range(2,98):
            fn = fn1 + fn2
            if fn==n:
                return True
            fn2 = fn1
            fn1 = fn   # cập nhật giá trị
        return False

def S(n):
    # Trường hợp cơ sở
    if n == 1:
        return -1
    # Nếu n chẵn
    if n % 2 == 0:
        return S(n - 1) + n
    # Nếu n lẻ
    else:
        return S(n - 1) - n

# Test

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def check(arr):
 for i in range(len(arr)):
    if i%2==0 and arr[i]%2==0:
         return True
    else:
        return False
import math
def nguyento(n):
    if n<2:
        return False
    else:
        for i in range(2,math.isqrt(n)+1):
            if n%i==0:
                return False
        return True
def chinhphuong(n):
        can=math.isqrt(n)
        if can*can==n:
            return True
        else:
            return False

if __name__ == "__main__":
    n=int(input())
    a=(list(map(int,input().split())))
    count=0
    dem=0
    dem1=0
    dem2=0
    for i in range(len(a)):
        if nguyento(a[i]):
            count+=1
    for i in range(len(a)):
        if rev(a[i]):
            dem2+=1  
    for i in range(len(a)):
        if chinhphuong(a[i]):
            dem+=1
    for i in range(len(a)):
        if nguyento(tongchuso((a[i]))):
            dem1+=1
    print(count,dem2,dem,dem1,end="\n")
