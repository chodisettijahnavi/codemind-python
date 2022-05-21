n=int(input())
temp=n
rev=0
while n>0:
    r=n%10
    n=n//10
    print(r,end='')