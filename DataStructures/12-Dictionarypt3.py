dog = {
    'type': 'Dog',
    'owner': 'Alice'
}

cat = {
    'type': 'Cat',
    'owner': 'Bob'
}

rabbit = {
    'type': 'Rabbit',
    'owner': 'Charlie'
}

pets = [dog, cat, rabbit]

for pet in pets:
    print("Type:", pet['type'])
    print("Owner:", pet['owner'])
