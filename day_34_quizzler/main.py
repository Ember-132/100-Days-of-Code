from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Interface

# add Question objects containing questions and answers to the question bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# start the quiz with questions in the bank
quiz = QuizBrain(question_bank)
window = Interface(quiz)
