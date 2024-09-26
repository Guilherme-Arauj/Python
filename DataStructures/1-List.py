list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]

#a) Biggest number on the list
biggest = int(max(list))
print(f"a) {biggest}")
print("-----------------")

#b) Smallest number on the list
smallest = int(min(list))
print(f"b) {smallest}")
print("-----------------")

#c) Only even numbers
print("c)", end = "")
for e  in list:
    if e % 2 == 0:
        print(e, end = " ")

print("-----------------")

#d) Number of occurrences of the first element in the list
count = 0 
firstElement = list[0]
for e in list:
        if e == firstElement:
            count += 1

print("d)", end = "")
print(count)
print("-----------------")

#e) Average
media = sum(list) / len(list) 
print("e)", end = " ")
print(f"Average:{media:.2f}")
