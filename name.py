#this program says hello and asks for name

#greets user
print('Hello world!')

#asks for name
print('What is your name?')

#saves name as var and ensures that entry is string
name = str(input())

#responds to input of name
print('It is good to meet you, ' + name + ' !')

#prints length of input
print('The length of your name is: ' + str((len(name))))

#asks for age
print('How old are you? ')

#save age as var and makes sure that entry is whole number
age = int(input())

#prints response and converts int to str
print('So, your name is ' + name + ' and you are ' + str(age) + ' years old.')
