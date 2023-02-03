from collections import Counter, defaultdict, OrderedDict
import pyjokes

joke = pyjokes.get_joke('en')
print(joke)


li = [1, 2, 2, 3, 42, 1, 1, 1, 1]
sentence ='I want to sleep'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda:'dpesn\'t exist',{'a': 1, 'b':2}) # give any value, 
print(dictionary['g'])
print(dictionary['a'])

d = OrderedDict() #retains the order you insert into a dictionary 

d['b']=2
d['a']=1

d2 = OrderedDict() #retains the order you insert into a dictionary 
d2['a']=1
d2['b']=2

print(d2==d)

#if it was a 'regular' dictionary, the order wouldn't matter
# because the dictionary is unordered
# Recently, the Python has made Dictionaries ordered by default! So unless you need to maintain older version of Python (older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!

import datetime

print(datetime.time(5,45,2))
print(datetime.date.today())

from array import array 
arr = array('I', [1,2,3]) #I for unsigned integers 
print(arr[0])