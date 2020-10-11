#this takes in a name and age from the user
#and also gives the length of the name

#gets user to input name and age
name = str(input('What is your name? '))
age = int(input('How old are you? '))

#takes name and finds length
def name_length(name):
    length_of_name = len(name)
    #prints results
    print('Your name is ' + name + ' and you are ' + str(age) + ' years old. The length of your name is ' + str(length_of_name) + '.') 

#calls function
name_length(name)
