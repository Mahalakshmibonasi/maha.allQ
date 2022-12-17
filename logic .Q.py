# '''loop question'''

# a=int(input("enter the num"))
# i=0
# sum=0
# while i<a:
#     n=int(input("enter the no"))
#     sum=sum+n
#     i+=1
# print(sum)

a=["abc","aba","cdc","abcd"]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[0]==a[2]:
            # print("true")
            b.append("true")
        else:
            print("false")
        j=j+1
    i=i+1   
