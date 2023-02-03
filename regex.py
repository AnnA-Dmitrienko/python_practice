import re

pattern = re.compile('inside')
string ='search inside of this text please'

# a= re.search('inside', string)
a= pattern.search(string)
print(a.span())
print(a.start())
print(a.start())
print(a.end())
print(a.group())
b=pattern.findall(string)
print(b)
c=pattern.fullmatch(string)#only for 100% match 
d= pattern.match(string)