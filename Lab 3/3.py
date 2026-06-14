num = int(input("Enter a number: "))
exp = int(input("Enter the exponent: "))

result = 1
for i in range(exp):
    result *= num
print(result)