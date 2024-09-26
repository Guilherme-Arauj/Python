sandwich_orders = ['Turkey', 'Ham', 'Veggie', 'Tuna', 'Chicken']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print("Preparing your", sandwich, "sandwich.")
    finished_sandwiches.append(sandwich)

print("Finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
