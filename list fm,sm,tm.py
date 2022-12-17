a=[12,34,56,78,65,87]
fm=0
sm=0
tm=0
i=0
while i<len(a):
    if a[i]>fm:
        fm=a[i]
    i+=1
i=0
while i<len(a):
    if a[i]>sm and a[i]!=fm:
        sm=a[i]
    i+=1
i=0
while i<len(a):
    if a[i]>tm and a[i]!=fm and a[i]!=sm:
        tm=a[i]
    i=i+1
print(fm,sm,tm)
