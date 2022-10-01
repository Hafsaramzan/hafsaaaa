myList=[]
print("Enter elements of first array")
for i in range (5):
    val=int(input("Enter elements of array"))
    myList.append(val)
myList2=[]
print("Enter elements of first array")
for i in range (5):
    val2=int(input("Enter elements of array"))
    myList2.append(val2)
myList3=myList+myList2
print(myList3)


def isPlaindrome(word):
    temp=word[::-1]
    if temp.capitalize()==word.capitalize():
        return True
    else:
        return False
print(isPlaindrome("deed"))


A= [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
B = [[5,8,1],
    [6,7,3],
    [4,5,9]]
C= [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(3):
   for j in range(3):
        for k in range(3):
           C[i][j] += A[i][k] * B[k][j]

for r in C:
   print(r)


def perimeter (listing):
    leng=len(listing)
    perimeter=0
    for i in range(0,leng-1):
        dis=(((listing[i][0]-listing[i+1][0])**2)+((listing[i][1]-listing[i+1][1])**2)**0.5)
        perimeter+=dis
        perimeter+=(((listing[0][0]-listing[leng-1][0])**2)+((listing[0][1]-listing[leng-1][1])**2)**0.5)
        return perimeter
l=[(1,3),(2,7),(3,9),(-1,8)]
print(perimeter(l))


def symmetric(a,b):
    e=set()
    for i in a:
        if i not in b:
            e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e
set1={0,1,2,3,4,5}
set2={6,7,8,9,0,1}
print (symmetric(set1,set2))


firstName=("shoaib","saqib","laiba")
lastName=("ali","hassan","shahid")
sample={("shoaib","ali"):"03124852197",("saqib","hassan"):"03122292552",("laiba","shahid"):"03115017560"}
searchtuple=("laiba","shahid")
if searchtuple in sample:
    print(sample[searchtuple])
else:
    print("NOT FOUND")

myList=[]
print("Enter elements of first array")
for i in range (5):
    val=int(input("Enter elements of array"))
    myList.append(val)
myList2=[]
print("Enter elements of first array")
for i in range (5):
    val2=int(input("Enter elements of array"))
    myList2.append(val2)
myList3=myList+myList2
myList3.sort()
print(myList3)


myList=[]
print("Enter elements of first array")
for i in range (5):
    val=int(input("Enter elements of array"))
    myList.append(val)
myList2=[]
print("Enter elements of first array")
for i in range (5):
    val2=int(input("Enter elements of array"))
    myList2.append(val2)
myList3=myList+myList2
maxi=myList3[0]
for i in range (10):
    for j in range (10):
        if (myList3[j]>maxi):
            maxi=myList3[j]
print (maxi)
mani=myList3[0]
for i in range (10):
    for j in range (10):
        if (myList3[j]<mani):
            mani=mylist3[j]
print(mani)


Dict={("laiba"):"5-02-2003",("hafsa"):"3-02-2004",("kiran"):"6-07-2002"}
print ("Welome to the birthday dictionary")
print("we know the birthdays of")
print("laiba")
print("kiran")
print("hafsa")
print("Enter the name of the person whose birthday you want to know")
name=str(input())
print(Dict[name])



Dict={("name"):"kelly",("age"):"25",("salary"):"260000",("city"):"new york"}
print(Dict['name'])
print(Dict['salary'])

from math import *
x=0.001
for i in range(0,360,30):
    print ("The value of sin and cos at ",i)
    a=((sin(i+x)-(sin(i)))/x)
    print("value of sin ",a)
    print("value of cos ",cos(i))





