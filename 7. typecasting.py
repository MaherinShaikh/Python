#the conversion of 1 Dt to another Dt is called typecasting

a = 1  #int
print(a)
b = 2
print(b)
print(a+b)

c = "1"
d = "2"
print(c+d)  #string concatenation

# e = "1"
# f = 2
# print(e+f)  #error

e = "1"
f = 2
print(int(e)+int(f))  #typecasting string to int

#explicit typecasting - programmer does it on own purposely
#implicit typecasting - python does it automatically -- lower order converted to higher order DT

g = 1.5  #float
h = 2   
print(g+h)  #int converted to float automatically
