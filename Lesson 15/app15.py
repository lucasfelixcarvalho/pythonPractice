def max_number(number_1, number_2, number_3):
    if number_1 >= number_2 and number_1 >= number_3:
        return number_1
    elif number_2 >= number_1 and number_2 >= number_3:
        return number_2
    else:
        return number_3


print(max_number(7, 6, 5))
