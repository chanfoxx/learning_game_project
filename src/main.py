from utils import *
from random import shuffle


# Выводим список вопросов из файла.
questions = get_list_questions(open_questions('all_questions.json'))

# Перемешиваем список.
shuffle(questions)

# Задаем вопросы и проверяем правильность ответов.
for question in questions:
    question.ask_question()
    question.get_answer()

# Выводим статистику.
print(get_statistics(questions))
