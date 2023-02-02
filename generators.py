def generator_function(number):
    for i in range(number):
        yield i * 2  # pauses the function and comes back to it


g = generator_function(100)
next(g)
next(g)
print(next(g))
print(next(g))

# EXAMPLE 1


def special_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break


special_for_loop([1, 2, 3])


# EXAMPLE 2
class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # this line allows us to use the current number as the starting point for the iteration
        MyGen.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 100)
for i in gen:
    print(i)


# Fibonacci example with generator
# def fib(number):
#     a =0
#     b=1
#     for i in range(number):
#         yield a
#         temp = a
#         a=b
#         b= temp+b

# for x in fib(21):
#     print(x)


def fib(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp+b
    return result


print(fib(1000))
