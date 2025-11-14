rows = int(input("Enter the Number of rows you want : "))

for i in range(rows):
    for j in range(rows - i - 1):
        print(end=" ")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

