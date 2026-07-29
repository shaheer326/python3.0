print("half pyramid pattern of stars (*)")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i +1):
        print("*", end="")
    print()

rows = int(input("please enter the total number of rows: "))
number = 1

print("floyd's triangle")
for i in range (1, rows +1):
    for j in range(1, i +1):
        print(number, end=" ")
        number += 1
    print()