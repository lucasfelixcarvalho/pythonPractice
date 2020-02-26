# from this link: https://www.youtube.com/watch?v=yeCsuIk9vp0&t=1729s

from collections import defaultdict

def main():
    values = [[1, 2, 3, 3], [1, 2, 3], [3, 1, 4, 57, 4], []]

    for a in values:
        print(f'List: {a}')

        most_frequent = return_most_frequent_1(a)
        print(f'Most frequent 1: {most_frequent}')

        most_frequent = return_most_frequent_2(a)
        print(f'Most frequent 2: {most_frequent}')
        
        print('----------------------------------')
    
'''
Get the most frequent integer.
Loop once and for each integer, add a 'x' value to a dictionary. At the end, the key (integer in list) with the greater string length is the most frequent integer.
Sort the result dictionary based on the value in DESC, so the key with the bigger string will be the first, return it.
Loop again the dictionary until we find the value that matches the biggest string.
'''
def return_most_frequent_1(values):
    if values == []:
        return None

    val_dict = defaultdict(str)
    
    for v in values:
        val_dict[v] += 'x'

    biggest_string = sorted(val_dict.values(), key=len, reverse=True)[0]

    for k, v in val_dict.items():
        if v == biggest_string:
            return k

'''
Get the most frequent integer by looping once in the list.
Count the number of elements looped. If the element being observed is equal to the last value and it's not the last element, just continue.
If not, check if the count of elements looped is greater than the most frequent count recorded, if yes, it means that we found a new most common integer.
In this case, update the number of elements (count_most_frequent), the integer which it refers to (most_frequent), and begin again the loop.
'''
def return_most_frequent_2(values):
    if values == []:
        return None

    most_frequent = None
    count = 0
    count_most_frequent = 0

    values.sort() # we need a sorted list to guarantee that when the element changes, there is no element further in the list
    last_value = values[0] # start with the first element

    for i, v in enumerate(values[1:], start=1): # ignore the first element
        count += 1
        
        if v == last_value and i != (len(values) - 1):
            continue
        else:
            if count >= count_most_frequent:
                most_frequent = last_value
                count_most_frequent = count
            count = 0

        last_value = v

    return most_frequent

if __name__ == "__main__":
    main()