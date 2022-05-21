def fibi(n):
    while n<=1:
        return n
    return fibi(n-1)+fibi(n-2)
n=int(input())
for i in range(n):
    print(fibi(i),end=' ')