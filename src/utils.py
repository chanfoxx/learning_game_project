import json
from question import Question


def open_questions(file_name):
    """Читаем вопросы из файла разрешением json."""
    with open(file_name, encoding='utf-8') as file:
        list_questions = json.load(file)
        return list_questions


def get_list_questions(list_questions):
    """Создаем список экземпляров класса вопросов."""
    questions = []
    for question in list_questions:
        questions.append(Question(question["q"], int(question["d"]), question["a"]))
    return questions


def get_statistics(questions):
    """Считает и вывыдит статистику."""

    questions_count = len(questions)
    correct_count = sum([quest.is_correct() for quest in questions])
    total_count = 0
    for question in questions:
        if question.is_right_answer:
            total_count += question.get_points()

    return f"""That's all!
You answered {correct_count}/{questions_count} correctly.
Your score: {total_count}."""
