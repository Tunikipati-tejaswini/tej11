print("input format")
c=0
n=int(input())
i=1
while i<=n:
    if n%i==0:
        c=c+1
    i+=1
print(c)
