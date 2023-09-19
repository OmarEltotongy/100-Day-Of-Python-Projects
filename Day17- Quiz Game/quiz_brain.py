from question_model import Question


class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list

    def next_question(self):
        input(f"Q.{self.question_num+1} : {self.question_list[self.question_num].question} (True/False): ")
        self.question_num += 1

    def still_has_questions(self):
        if (len(self.question_list)) == self.question_num:
            return False
        else:
            return True


 #   def evaluate_answer(self, ):
