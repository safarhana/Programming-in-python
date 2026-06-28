numbers = list(map(int, input("Enter numbers: ").split()))

key = int(input("Enter a number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Number found at index", i)
        found = True
        break

if not found:
    print("Number not found in the list.")