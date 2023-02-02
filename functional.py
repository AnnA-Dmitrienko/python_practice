from functools import reduce

# my_list = [1,2,3]
# your_list = [10,20,30, 50]

# def multiply_by2(item):
#     return item*2

# map(multiply_by2, [1,2,3])

# print(list(map(multiply_by2, [1,2,3])))


# def only(item):
#     return item %2 !=0


# print(list(filter(only, [1,2,3])))
# print(list(zip(my_list, your_list)))


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(str):
    return str[0].upper()+str[1:]


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
srt = my_numbers[::-1]
print(list(zip(srt, my_strings)))
print(list(zip(sorted(my_numbers), my_strings)))


# 3 Filter the scores that pass over 50%
def passScore(num):
    return num > 50


scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(passScore, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
combined_list = my_numbers+scores
print(combined_list)


def accumulator(acc, item):
    return acc+item


print(reduce(accumulator, combined_list, 0))
print(reduce(accumulator, (my_numbers+scores)))

anna_list = [5, 4, 3]
print(list(map(lambda item: item**2, anna_list)))


# list sorting
a = [(0, 2), (4, 3),  (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])  # common way to adjust sorting
print(a)

# list comprehensions
# generate a list based on requrements
# my_list = [param for param in iterable ]
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num*2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100)
            if num % 2 == 0 and num % 5 == 0]
print(my_list4)


# set comprehemsions - same as list

# dictionary comprehensions
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()
           if value % 2 == 0}  # items() for dict key values
my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)

# ----------------------------------------------------

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

duplicates_improved = list(
    set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates_improved)
