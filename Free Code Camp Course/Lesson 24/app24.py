try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("ZeroDivisionError")
        value = 10/0
    else:
        print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
