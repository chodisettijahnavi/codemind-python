n=int(input())
cpy=n
ds=0
while n:
    ds+=n%10
    n//=10
if cpy%ds==0:
    print('True')
else:
    print('False')