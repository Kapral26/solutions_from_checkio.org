import re

l = "greetings, friends"
k = "don't touch it"
o = "Hello.world"

parser = re.search("[A-z']+", o)
# print(parser)
print(parser.group())