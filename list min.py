a=[1,2,3,4,5]
i=0
min=a[0]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
print(min)