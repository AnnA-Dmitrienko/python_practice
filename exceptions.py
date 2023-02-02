# Error handling

# while True:
#     try:
#         age =int(input('what is your age? '))
#         10/age
#     except ValueError: ##handle only value errors
#         print('please enter a number')
#     except ZeroDivisionError: ##handle only zero division error
#         print('please enter age higher than 0')
#     else:
#         print('Thank you')
#         break


# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f'please enter numbers {err}')

# print(sum('1', 2))



def divide(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)

print(divide('1', 2))
print(divide(1, 0))



# while True:
#     try:
#         age =int(input('what is your age? '))
#         10/age
#     except ValueError: ##handle only value errors
#         print('please enter a number')
#         continue
#     except ZeroDivisionError: ##handle only zero division error
#         print('please enter age higher than 0')
#         break
#     else:
#         print('Thank you')
#         break
#     finally: #no matter what, at the end of it all - do smth
#         print('ok, i am finally done')
#     print('can you hear me')

    
#customize your own error 
while True:
    try:
        age =int(input('what is your age? '))
        10/age
        raise ValueError('hey this is an ERROR!')
        # raise Exception('hey this is an EXCEPTION!') #EITHER OR 
    # except ValueError: ##handle only value errors
    #     print('please enter a number')
    #     continue
    except ZeroDivisionError: ##handle only zero division error
        print('please enter age higher than 0')
        break
    else:
        print('Thank you')
        break
    finally: #no matter what, at the end of it all - do smth
        print('ok, i am finally done')
    print('can you hear me')