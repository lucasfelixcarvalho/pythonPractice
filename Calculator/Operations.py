def add(num1, num2):
    result = float(num1) + float(num2)
    if __return_float(num1) and __return_float(num2):
        return float(result)
    else:
        return int(result)


def subtract(num1, num2):
    result = float(num1) - float(num2)
    if __return_float(num1) and __return_float(num2):
        return float(result)
    else:
        return int(result)


def multiply(num1, num2):
    result = float(num1) * float(num2)
    if __return_float(num1) and __return_float(num2):
        return float(result)
    else:
        return int(result)


def divide(num1, num2):
    if int(num2) == 0:
        return "Divide by zero not possible"
    else:
        result = float(num1) / float(num2)
        return float(result)


def change_signal(number):
    if __return_float(number):
        return float(number) * (-1)
    else:
        return int(number) * (-1)


def __return_float(number):
    return isinstance(number, float)
