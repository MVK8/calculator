
print("""Welcome to this simple calculator.
Use [ + ] for adding
Use [ - ] for subtracting.
Use [ * ] for multiplying
Use [ / ] for dividing """)

x, x2, x3 = input("Expression:").split()

y = float(x)

y2 = float(x3)

if x2 == "+":
    z = y + y2

elif x2 == "-":
    z = y - y2

elif x2 == "*":
    z = y * y2

elif x2 == "/":
    z = y / y2

else:
    print("Error, are you sure you typed it correctly?")

z = int(z) if z.is_integer() else z

print(z)

