'''k=int(input("k: "))
sum1=0
a=0
b=1
count=0
s=0
while(sum1<k):
    print(sum1)
    a=b
    b=sum1
    sum1=a+b
    if(count%2==0):
        s+=b
    count+=1
print("sum:",s)

k=int(input("k: "))
i=0
while(i<k):
    if(i%2==0):
        print(i,"even number")
    else:
        print(i,"odd number")
    i+=1'''

num=int(input())
for i in range(1,num+1,2):
    print(i)
    

