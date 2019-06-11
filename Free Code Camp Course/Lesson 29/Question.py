class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def is_answer_correct(self, user_answer):
        return self.answer.lower() == user_answer.lower()
