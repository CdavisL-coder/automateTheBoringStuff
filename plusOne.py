#adds one to a number
#if number % 3 or 4 = 0, double number

#this function takes in a parameter
def plus_one(num):
    num = num + 1
    #if parameter is divided by 2 and equal zero, the number is doubled
    if num % 2 == 0:
        num2 = (num + 1) * 2
        print(num2)
    #else print the number
    else:
        print(num)

plus_one(4)
plus_one(80)
plus_one(33)
