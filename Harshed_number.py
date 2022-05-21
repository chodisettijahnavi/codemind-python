n=int(input())
s=0
temp=n
while n:
    r=n%10
    s=s+r
    n=n//10
if(temp%s==0):
    print(True)
else:
    print(False)