# @classmethod
# @staticmethod

# Decorator


from time import time


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator
def hello(greeting='****', emoji=':)))'):
    print(greeting, emoji)


hello('Anna says hello')
hello()

# Decorators practice


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


def performace(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} ms')
        return result
    return wrap_func


@performace
def long_time():
    for i in range(1000000):
        i*5


long_time()


# Exercise
# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fun):
    def wrap_func(*args, **kwargs):
        if args[0]['valid']:
            return fun(*args, **kwargs)
        return print("NO!")
    return wrap_func


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
