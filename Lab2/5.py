mark = int(input("Enter your mark: "))

if mark >= 90:
    Grade = "A+"
elif mark >= 85:
    Grade = "A"
elif mark >= 80:
    Grade = "A-"
elif mark >= 75:
    Grade = "B+"
elif mark >= 70:
    Grade = "B"
elif mark >= 65:
    Grade = "C+"
elif mark >= 60:
    Grade = "C"
elif mark >= 55:
    Grade = "D+"
elif mark >= 50:
    Grade = "D"
else:
    Grade = "F"

print(Grade)
