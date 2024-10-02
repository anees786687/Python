class QuizBrain:
    def __init__(self, question_bank) -> None:
        self.score = 0
        self.question_number = 0
        self.question_bank = question_bank

    def next_question(self):
        ques = self.question_bank[self.question_number]
        self.question_number += 1
        ans = ""

        while ans != "true" and ans != "false":
            ans = input(f"{ques.text}. True or False: ").lower()
            if ans != "true" and ans != "false":
                print("Please enter either True or False")

        if ans == ques.ans.lower():
            self.score += 1
            print(f"Correct! Your score is {self.score}/{self.question_number}")
        else:
            print(f"Wrong! Your score is {self.score}/{self.question_number}")

       


    def still_has_questions(self):
        return self.question_number != len(self.question_bank)