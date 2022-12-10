'''num=int(input("num: "))
if(num%3==0):
    print("number is divisible by 3")
print("END")




marks=int(input("Marks: "))
distinction_marks=75
if(marks>distinction_marks):
    print("distinction")
else:
    print("No need to study")




num=int(input("Enter a number: "))
if(num>0):
    print("positive")
elif(num<0):
    print("negative")
else:
    print("zero") 




print("0 for exit")
ch=input("ch: ")
if ch== '0':
    exit()
elif((ch>='a' and ch<='z')or(ch>='A' and ch<='Z')):   #(ch.isalphabet()) for shortcut
    print("alphabet")
elif(ch.isdigit()):
    print("digit")
else:
    print("neither alphabet nor digit ")




a=int(input("Enter a year: "))
if(a%400==0)and(a%100==0):
    print("Leap year")
elif(a%4==0)and(a%100!=0):
    print("Leap year")
else:
    print("Not a leap year")


i=1
while(i<=10):
    print(i)
    i+=1


import math
a=int(input("x: "))
b=int(input("y: "))
if((a==0) or (b==0)):
    print("value must be non zero")
else:
    rem=a%b
    while rem!=0:
        a=b
        b=rem
        rem=a%b
    print("gcd:",b)   #or 
c=math.gcd(a,b)
print(c)'''




k=int(input("k: "))
sum1=0
a=0
b=1
count=1
while(count<=k):
    count+=1
    a=b
    b=sum1
    sum1=a+b
    print(sum1)





    









