#this program simulates rolling dice

#this imports the random module
import random

#this sets the value of dice to 2 (how many times to roll or two dice)
dice_roll = 2

#while dice_roll less than or equal to 2, do x
while dice_roll <= 2:
    dice = random.randint(1,20)
    dice_two = random.randint(1,20)
    #if dice is equal to dice 2, double the value
    if dice == dice_two:
        dice = dice * 2
        dice_two = dice_two * 2
        #notifies user when dice is the same number
        print('You hit doubles, so values are doubled!')
    dice_roll = dice_roll + 1
    print('You rolled ' + str(dice) + ' and ' + str(dice_two) + '!')
    
