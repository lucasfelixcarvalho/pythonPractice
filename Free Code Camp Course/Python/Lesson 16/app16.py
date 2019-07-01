num_1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num_2 = float(input("Enter second number: "))

if op == "+":
    print(num_1 + num_2)
elif op == "-":
    print(num_1 - num_2)
elif op == "/":
    print(num_1 / num_2)
elif op == "*":
    print(num_1 * num_2)
else:
    print("Invalid operator")


