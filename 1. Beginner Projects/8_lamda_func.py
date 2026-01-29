# Here is an example of the lamda function
x = int(input("Enter the number you want to square: "))
square = lambda x:x*x
print(square(x))

"""
Here to call the lambda function we cannot use
print(square) like the normal function which calls and then assigns the value to the variable.
But we do like 

print(square(x)) where x is the parameter. It is because by usning lambda we make square like
another function. So we need to call square(parameter).

"""