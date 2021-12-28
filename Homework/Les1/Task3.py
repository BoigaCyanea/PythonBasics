n = input("Enter the integer number: ")

while n < '0':
    print("I need an integer")
    n = input("Enter a number greater than 0")

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")