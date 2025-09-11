


class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_answer = None
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        while user_answer != 't' and user_answer != 'f':
            if user_answer is not None:
                print("Please enter 't' or 'f' only.")
            user_answer = input(f"{self.question_number}: {current_question.text}. True or False? Type 't' or 'f': ").lower()
        
        if user_answer == 't':
            user_answer = 'True'
        elif user_answer == 'f':
            user_answer = 'False'

        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong :(")
        print(f"Correct answer : {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")