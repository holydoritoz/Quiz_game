from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    q_text = i['question']
    q_answer = i['correct_answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print('You have completed the quiz!')
print(f'Your final score was: {quiz_brain.score}/{quiz_brain.question_number}')

