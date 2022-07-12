def func(b,r):
    for val in b:
        if val < 2:
            return r
        if val % 2 != 0:
            return r
    r += 1
    return func(list(map(lambda x: x / 2,b)),r)

a = input() #これどうつかうんだ？
b = list(map(int, input().split())) 
r = 0
print(func(b,r))

    

