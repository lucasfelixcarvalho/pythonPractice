def add(num1, num2):
    num1 = __convert_to_number(num1)
    num2 = __convert_to_number(num2)
    return num1 + num2


def subtract(num1, num2):
    num1 = __convert_to_number(num1)
    num2 = __convert_to_number(num2)
    return num1 - num2


def multiply(num1, num2):
    num1 = __convert_to_number(num1)
    num2 = __convert_to_number(num2)
    return num1 * num2


def divide(num1, num2):
    try:
        num1 = __convert_to_number(num1)
        num2 = __convert_to_number(num2)

        temp_result = num1 / num2
        if temp_result == int(temp_result):  # Example: 2 / 2 returns 1 instead of 1.0; 2 / 3 still returns 0.6666...
            result = int(temp_result)
        else:
            result = temp_result

        return result
    except ZeroDivisionError:
        return "Division by zero not possible"


def change_signal(number):
    number = __convert_to_number(number)
    return number * (-1)


def __convert_to_number(text_input):  # all inputs from the calculator comes as string, so we convert to number
    try:
        if "." in text_input:
            return float(text_input)
        else:
            return int(text_input)
    except ValueError:
        return 0
