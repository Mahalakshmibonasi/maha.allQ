# a=[1,2,3,4,5,6]
# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
#         secondmax=max
#         max=a[i]
#     i=i+1
# print(secondmax)


# a=[2,3,2,[5,1,2],[1,2,3],3]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a):
#         if type(a[i])==list:
#             sum=sum+a[i][j]
#             j=j+1
#         b.append(sum)
#         i=i+1
#     print(b)

# i=10
# while i<=1:
#     print(i)
#     i=i-1

a=["simi","sum1@23"]
i=0
b=[]
while i<len(a):
    j=0
    s=" "
    while j<len(a[i]):
        if a[i][j]>="a" and a[i][j]<="z":
            s=s+a[i][j]
            j=j+1
        b.append(a)
        i=i+1
    print(b)    

# a=[2,3,4,[5,1,2],[1,2,3],1]
# i=0
# m=0
# l=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         m2=0
#         l2=[]
#         while j<len(a[i]):
#             m2+=a[i][j]
#             j=j+1
#         l2.append(14)
#     else: ``
#         m=m+a[i]
#     i=i+1
#     l2.append(m)
#     l2.append(l2)
# print(l2)
    

# a=int(input("enter the num"))
# if a>0:
#     print(-a)
# else:
#     print(a)

# i=0
# while i<=5:
#     j=0
#     while j<=i:
#         print(j**1,end="")
#         j=j+1
#     print()
#     i=i+1
