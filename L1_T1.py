number = input("Enter number: ")
try:
    new_num = int(number) + 2
    print(f"{number} + 2 = {new_num}")
except ValueError as t:
    print(t)
