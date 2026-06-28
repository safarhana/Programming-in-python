numbers = [10, 20, 30, 20, 50]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List after removing duplicates:", result)