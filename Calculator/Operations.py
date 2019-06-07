def add(num1, num2):
    result = float(num1) + float(num2)
    if __return_float(num1, num2):
        return float(result)
    else:
        return int(result)


def subtract(num1, num2):
    result = float(num1) - float(num2)
    if __return_float(num1, num2):
        return float(result)
    else:
        return int(result)


def multiply(num1, num2):
    result = float(num1) * float(num2)
    if __return_float(num1, num2):
        return float(result)
    else:
        return int(result)


def divide(num1, num2):
    if int(num2) == 0:
        return "Divide by zero not possible"
    else:
        result = float(num1) / float(num2)
        return float(result)


def __return_float(number1, number2):
    return isinstance(number1, float) and isinstance(number2, float)
