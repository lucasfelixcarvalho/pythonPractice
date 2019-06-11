from Question import Question

questions_to_user = [
    Question("What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n", "a"),
    Question("What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n", "c"),
    Question("What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n", "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if question.is_answer_correct(user_answer):
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions_to_user)
