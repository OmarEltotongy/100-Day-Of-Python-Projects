from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for count in range(0, len(question_data)):
    question_bank.append(Question(question_data[count]["text"], question_data[count]["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
