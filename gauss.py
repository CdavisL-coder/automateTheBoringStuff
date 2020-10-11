#this program adds all number from 0 - 100

#sets the starting value for num
num = 0

#for numbers up to 50
for i in range(50):
    #add 1 to number for each iteration
    num = num + 1
    #multiply number by 100 and add 50 each time
    total = num * 100 + 50
    #print result
    print(total)
