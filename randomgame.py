from random import randint
# generate number 1-10
answer = randint(1, 10)
# input from user

# check that input is a number 1-10
while True:
    try:
        print(answer)
        guess = int(input('guess a number 1-10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('all good')
            break
    except ValueError:
        print('please enter a number')
        continue

# check if number is right quess
# otherwise - check again
