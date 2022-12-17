# def fun(a):
#     a=5
# fun(a)


# def fun(a,b):
#     # a=5
#     # b=6
#     c=a+b
#     print(c)
# fun(5,6)

# def fun(a,b):
#     a=5
#     b=6
#     c=a+b
#     return c
# print(fun(5,6))


# a=2
# b=10
# def fun(A):
#     print(a)
# c=a+b
# print(c)
# fun(4)


# # a=[2,4,[3,2,4,1],4,1]
# a=[1,4,5,[6,7,8,[9,10],11,12],13,14]
# i=0
# # s2=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         s=0
#         # l=[]
#         while j<len(a[i]):
#             # s+=a[i][j]
#             j+=1
#     else:
#         i=i+1
#         # s2+=a[i]
#         # i+=1
#     # b.append()
#         # i=i+1# b.append(l)
#     print(b)

# a=[0,1,2,3,0,0,5,0]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]!=0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b+c)

# a=[2,3,2,5,6,2,2]
# i=0
# c=0
# l=[]
# while i<len(a):
#     u=a.count(a[i])
#     if u==1:
#         l.append(a[i])
#     i+=1
# print(l)

    
# i=0
# while i<=6:
#     j=0
#     while j<=i:
#         if j%2!=0:
#             print(j,end="")
#             j=j+1
#         else:
#             print(0,end="")
#     print()
#     i=i+1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j=j+1
#     i=i+1
#     print()

# a=int(input("enter the num"))
# if a>0:
#     print(-a)
# else:
#     print(a)

# a=[1,2,3]
# b=[1,2,3]
# x=a
# print(a is b)
# print(b is x)

# a=True
# b=False
# print(a and b or a and b)

# a=-18//4
# print(a)

# a="simi
# print(a*3)

# a=7
# b="simi"
# c="3"
# print(a*c)
# print(a+b+c)

# a=int(input("enter the num"))
# i=1
# while i<=10:
#     print(a,"*",i,"=",a*i)
#     i=i+1


a=[1,4,5,[6,7,8,[9,10],11,12],13,14]
i=0
b=[]
while i<len(a):
    if type(a[i])==0:
        j=0
        sum=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)

