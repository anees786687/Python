from data import question_data
from question_model import QuestionModel
import random
from  quiz_brain import QuizBrain

# make a list on Question objects
question_bank = []

for question in question_data:
    question_bank.append(QuestionModel(question["text"],question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
