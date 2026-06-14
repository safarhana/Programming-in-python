num = int(input("Enter a number: "))

a = 0
b = 1

while a < num:
    print(a)
    c = a + b
    a = b
    b = c