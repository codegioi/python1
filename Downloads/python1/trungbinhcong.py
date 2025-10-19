import math
def nguyento(n):
    if n<2:
        return False
    else:
        for i in range(2,math.isqrt(n)+1):
            if n%i==0:
                return False
        return True
def tongchuso(n):
    sum=0
    while n!=0:
        temp=n%10
        sum+=temp
        n=n//10
    return sum
def fibo(n):
    if n == 0:
        return True
    elif n == 1:
        return True
    else:
        fn1 = 0
        fn2 = 1 # fn1 = F1, fn2 = F0
        for i in range(2,100):
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

n=int(input())
arr=list(map(int,input().split()))
dem=0
tong=0
for x in arr:
    if nguyento(x):
        tong+=x
        dem+=1
print(f"{tong/dem:.3f}")
