lucky_numbers = [8, 23, 4, 16, 15, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]

print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append("Carol")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kelly"))
print(friends.count("Oscar"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
friends.clear()
print(friends)
print(friends2)
