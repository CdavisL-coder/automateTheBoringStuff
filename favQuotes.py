import random

def fav_quotes():
    print('These are my favorite quotes!')
    randomized = random.randint(1,4)
    if randomized == 1:
        print('Every breath you draw in my presence annoys me.')
    elif randomized == 2:
        print('No! Noooo! NOOOOO!!!')
    elif randomized == 3:
        print("Why are you booing!? I'm right!")
    else:
        print('Why would you say something so controversial and yet so brave!?')

fav_quotes()
fav_quotes()
fav_quotes()
