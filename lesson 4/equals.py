import re
from functools import reduce

file = open("privet.txt.")
s = reduce(lambda a, b: a + b, file.readlines())
sentences = filter(lambda a: a != "", re.split('[!.?]', s))
print(len(list(sentences)))