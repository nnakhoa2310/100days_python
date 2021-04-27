class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
    def stil_has_question(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("This answer is correct")
            self.score += 1
        else:
            print("U are stupid, that's wrong")
        print("Your current score is:", self.score,"/",self.question_number)