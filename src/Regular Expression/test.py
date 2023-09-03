import re

text = open("actual.txt","r")

numbers = []
for line in text:
    numbers.extend(re.findall("[0-9]+",line))
numbers2 = list(map(lambda x: int(x),numbers))
print(sum(numbers2))