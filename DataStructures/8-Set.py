#set A
setA = {'laranja', 'banana', 'uva', 'pera'}

#set B
setB = {'maçã', 'banana', 'kiwi', 'laranja'}

a = set(setA)
b = set(setB)

difference = a - b
union = a | b
intersection = a&b
symmetricDifference = a^b

print("Set A:", a)  
print("Set B:", b) 

print(difference, union, intersection, symmetricDifference)

