n,a,b = map(int,input().split())

r = 0
for i in range(1,n+1):
    t = map(int,list(str(i)))
    t = sum(t)
    if a <= t and b >= t:
        r += i

print(r)






