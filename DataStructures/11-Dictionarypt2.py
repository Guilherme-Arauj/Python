person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person3 = {
    'first_name': 'Emily',
    'last_name': 'Johnson',
    'age': 22,
    'city': 'Chicago'
}

people = [person1, person2, person3]

for person in people:
    print("First name:", person['first_name'])
    print("Last name:", person['last_name'])
    print("Age:", person['age'])
    print("City:", person['city'])
