# match statements
x = int(input("Enter a number: "))
match x:
    case 0:
        print("You entered zero")
    case 1:
        print("You entered one")
    case 2:
        print("You entered two")
    

    # case 0 | 1 | 2:
    #     print("You entered zero, one or two")   
    case _ if x!=20:
        print("You entered something other than zero, one, two or twenty")
    case _ if x==20:
        print("You entered twenty")

    case _:
        print("You entered something else")