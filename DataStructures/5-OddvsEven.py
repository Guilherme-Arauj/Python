V=[9,8,7,12,0,13,21]
evenList = []
oddList = []

#Only even numbers
print("Even List)", end = "")
for e  in V:
    if e % 2 == 0:
        e = evenList.append(e)

print(evenList)


#Only Odd numbers
print("Odd List)", end = "")
for e in V:
    if e % 2 != 0:
        e = oddList.append(e)

print(oddList)