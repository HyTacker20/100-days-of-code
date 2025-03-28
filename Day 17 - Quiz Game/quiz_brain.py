class QuizBrain:
    def __init__(self, question_list: list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False)?: ")
        if self.check_answer(answer, question.answer):
            self.question_number += 1
            return True
        return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score: {self.score}/{self.question_number+1}")
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number + 1 != len(self.question_list)
