num=int(input("enter any integer you want to reverse"))
reverse=str(num)
print(reverse[::-1])

num=int(input("enter how many number you want to add"))
sum=0
for i in range(num):
    num1=int(input("enter number"))
    sum=sum+num1
print("the sum of all numbers is",sum)

n=int(input("enter the number you want to find fibonacci series"))
a=0
b=1
c=1
print(a)
while c<n:
    print(c)
    c=a+b
    a=b
    b=c

marks=int(input("enter marks"))
if marks<50:
    print("fail")
elif marks>=50 and marks<=60:
    print("E")
elif marks>61 and marks<70:
    print("D")
elif marks>71 and marks<80:
    print("C")
elif marks>81 and marks<90:
    print("B")
elif marks>91 and marks<100:
    print("A")
else:
    print("please enter marks between 0-100")

num=int(input("enter a number you want to find a fictorial of"))
fact=1
for i in range(1,num + 1):
    fact=fact*i
print("factorial of",num,"is",fact)
     


