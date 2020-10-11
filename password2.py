#check password

#set value for password and tries
password = 'Shadows'
tries = 0

#directs user to enter password
print('Please enter your password. ')

#allows user to input info and converts to string
first_attempt = str(input())

#prints result
print(first_attempt)

#checks input from user
if first_attempt == 'Shadows':
    print('Access granted!')
else:
    while tries < 3:
        print('Please enter your password again.')
        try_again = str(input())
        if try_again == password:
                print('Access granted.')
                break
        print('Access denied.')
        tries = tries + 1
    
