def gmean(a,b):
    mean = (a*b)/(a+b)
    print("gmean: ",mean)


def greater(a,b):
    if a>b:
        print(a,"is greater than",b)
    elif a<b:
        print(b,"is greater than",a)
    else:
        print("Both numbers are equal")


def islesser(a,b):
    pass

a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))
gmean(a,b)
greater(a,b)

c = 7
d = 4
gmean(c,d)
greater(c,d)