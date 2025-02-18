def generate_random():
    return (hash(str(id(object())))) % 100 + 1

random_numbers = []
for _ in range(4):
    random_numbers.append(generate_random())

print("Random numbers:", random_numbers)
