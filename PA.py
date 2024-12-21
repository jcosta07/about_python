first = int(input('insert the first term: '))
r = int(input('insert the reason as well: '))
t = 0
c = r*10
for t in range(first, c, r):
    print(t)
    t +=(first+r)
print('End!')    