#this program finds the value of the magic stat as level increases

#sets the value of level and magic stat
level = 10
num = 116

#for level and magic stat within the range of 189
for i in range(189):
    #if level less than 100, increase level by 1 and num by 5
    if level <= 100:
        level = level + 1
        num = num + 5
    #if level greater than 100, increase level by 1 and num by 3
    elif level >= 100:
        level = level + 1
        num = num + 3
    #print results
    print('Your level has increased to ' + str(level) + '! Magic increased to ' + str(num) + '!')
