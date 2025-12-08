a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second value (b): ")

print(f"Original Values: a = {a}, b = {b}")

temp = a 
a = b 
b = temp

print(f"Swapped value: a = {a}, b = {b}")