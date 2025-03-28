from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(text[1], answer[1]) for text, answer in [data.items() for data in question_data]]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
