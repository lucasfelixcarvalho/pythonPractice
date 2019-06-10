def add(num1, num2):
    num1 = __convert_to_number(num1)
    num2 = __convert_to_number(num2)

    result = num1 + num2
    if __return_float(num1) or __return_float(num2):
        return float(result)
    else:
        return int(result)


def subtract(num1, num2):
    num1 = __convert_to_number(num1)
    num2 = __convert_to_number(num2)

    result = num1 - num2
    if __return_float(num1) or __return_float(num2):
        return float(result)
    else:
        return int(result)


def multiply(num1, num2):
    num1 = __convert_to_number(num1)
    num2 = __convert_to_number(num2)

    result = num1 * num2
    if __return_float(num1) or __return_float(num2):
        return float(result)
    else:
        return int(result)


def divide(num1, num2):
    try:
        num1 = __convert_to_number(num1)
        num2 = __convert_to_number(num2)

        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Divide by zero not possible"


def change_signal(number):
    number = __convert_to_number(number)

    if __return_float(number):
        return number * (-1)
    else:
        return number * (-1)


def __return_float(number):
    return isinstance(number, float)


def __convert_to_number(text_input):  # all inputs from the calculator comes as string, so we convert to number
    if "." in text_input:
        return float(text_input)
    else:
        return int(text_input)
