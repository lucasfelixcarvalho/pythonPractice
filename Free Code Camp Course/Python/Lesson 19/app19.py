secret_word = "giraffe"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess_word != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess_word = input("Enter an animal: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You tried too much")
else:
    print("You found it")
