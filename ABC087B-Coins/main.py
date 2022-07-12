A_COST = 500
B_COST = 100
C_COST = 50

a = int(input())
b = int(input())
c = int(input())
t = int(input())
r = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            sum = (i * A_COST) + (j * B_COST) + (k * C_COST)
            if sum == t:
                r += 1

print(r)

