s = input() 
d = {'a':s.count('a'),'b':s.count('b'),'c':s.count('c')}
print(max(d, key=d.get))