#this is to demonstrate error handling in python

#this function divides 42 by a value
def div42by(divideBy):
    #this tells the program to attempt to divide
    try:
        return (42/divideBy)
    #this tells the program to not divide by zero and to print an error message
    except ZeroDivisionError:
        print('ERROR! You can not divide by zero!')

print(div42by(2))
print(div42by(10))
print(div42by(12))
print(div42by(0))
print(div42by(1))
