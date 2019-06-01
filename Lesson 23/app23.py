def translate(phrase):
    vowels = ["a", "e", "i", "o", "u"]
    translation = ""
    for letter in phrase:
        if letter.lower() in vowels:
            if letter.islower():
                translation += "g"
            else:
                translation += "G"
        else:
            translation += letter
    return translation


print(translate(raw_input("Enter a phrase: ")))
