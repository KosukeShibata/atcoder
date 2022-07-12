n = int(input())
a = list(map(int,input().split()))
a.sort()

alice = 0
bob = 0
flag = True
for i in range(n-1,-1,-1):
    if flag :
        alice += a[i]
    else:
        bob += a[i]
    flag = not flag

print(alice - bob)

