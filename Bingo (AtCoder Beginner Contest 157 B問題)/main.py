a = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]
flag = False

#横の判定
for i in range(0,3):
    flag = True
    for j in range(0,3):
        if a[i][j] not in b:
            flag = False
            break
    if flag == True:
        print("Yes")
        exit()

#縦の判定
for j in range(0,3):
    flag = True
    for i in range(0,3):
        if a[i][j] not in b:
            flag = False
            break
    if flag == True:
        print("Yes")
        exit()

#斜めの判定
flag = True
pat_1 = [a[0][0],a[1][1],a[2][2]]
pat_2 = [a[0][2],a[1][1],a[2][0]]
for i in pat_1:
    if i not in b:
        flag = False
        break
if flag == True:
    print("Yes")
    exit()

for i in pat_2:
    if i not in b:
        flag = False
        break
if flag == True:
    print("Yes")
    exit()

print("No")

        