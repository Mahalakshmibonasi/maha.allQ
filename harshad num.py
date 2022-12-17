i=0
n=int(input("enter the num"))
z=n
sum=0
while i<=n:
    num=n%10
    sum=sum+sum
    n//10
print(sum)
if 2%sum==0:
    print("harshad no")
else:
    print("not harshad no")