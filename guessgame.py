from random import randint
a = 0
count = 0
r = randint(0, 10)
while count < 3:
    try:
        a = int(input('number?\n_'))
    except ValueError:
        print('Error! IsNaN.')
    if a == r:
        print('You win!!!')
        break
    elif r-2 <= a < r or r+2 >= a > r:
        print('You are getting hot! HOT! HOOOTT!')
    elif r-6 <= a < r-2 or r+6 >= a > r-2:
        print('You are getting warmer! Oh so warm :D')
        
