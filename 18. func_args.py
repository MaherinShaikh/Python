def average(a = 9, b = 1):
    print("average is: ", (a+b)/2)

average()  # This will use the default values of a and b
average(10)  # This will use 10 for a and the default value of b
average(10, 20)  # This will use 10 for a and 20 for b  

def name(fname, mname="john", lname="doe"):
    print("Full name is: ", fname, mname, lname)

name("Alice")  # This will use "Alice" for fname and the default values for mname and lname
name("Alice", "Smith")  # This will use "Alice" for fname, "Smith" for mname, and the default value for lname
name("Alice", "Smith", "Johnson")  # This will use "Alice" for fname, "Smith" for mname

# keyword arguments are a way to pass arguments to a function by explicitly specifying the parameter names. This allows you to provide values for specific parameters without relying on their order in the function definition. Keyword arguments enhance code readability and flexibility, especially when dealing with functions that have multiple parameters.

name(fname="Alice", mname="Smith", lname="Johnson")  # This will use "Alice" for fname, "Smith" for mname, and "Johnson" for lname

# required arguments are the parameters that must be provided when calling a function. If a required argument is not supplied, Python will raise a TypeError indicating that the function is missing a required positional argument. Required arguments are defined in the function signature without default values.


#variable length arguments are a way to allow a function to accept an arbitrary number of arguments. In Python, you can use *args for variable-length positional arguments and **kwargs for variable-length keyword arguments.

def average(*numbers):
        sum = 0
        for i in numbers:
            sum += i    
        print("average is: ", sum/len(numbers))

average(10, 20, 30)  # This will calculate the average of 10, 20, and 30

#return statement

def get_average(*numbers):
        sum = 0
        for i in numbers:
            sum += i
        return sum / len(numbers) if numbers else 0

result = get_average(10, 20, 30)
print("average is: ", result)

get_average(10, 20, 30)  # This will calculate the average of 10, 20, and 30