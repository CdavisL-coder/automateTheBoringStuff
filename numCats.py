#this program asks how many cats a person has

#this asks how many cats a person has
print('How many cats do you have?')

#this is the answer the user choses
num_Cats = input()

#try this if the answer is a number
try:
    if int(num_Cats) >= 0 and int(num_Cats) <= 2:
        print('That is not a lot of cats.')
    elif int(num_Cats) >= 3:
            print("That's a lot of dear little ones!")
    else:
        print("You don't have any cats and that's sad to be honest.")
#run this if answer is not a number
except ValueError:
    print('You did not enter a number.')
