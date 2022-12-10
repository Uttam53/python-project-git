'''def recurfact(n):
    if n==1:
        return n
    else:
        return n*recurfact(n-1)
n=int(input("num: "))
if (n<0):
    print("factorial does nor exist")
elif (n==0):
    print("factorial:1")
else:
    print("factorial",recurfact(n))'''


def add(x,y):
    if y==0:
        return x
    elif x==0:
        return y
    else:
        return (1+add(x,y-1))

a=int(input())
b=int(input())

print(add(a,b))
