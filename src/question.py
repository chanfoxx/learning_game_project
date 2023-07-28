class Question:
    """Модель для представления вопроса и проверки ответов."""
    question_text = None
    level = None
    answer = None

    is_asked = False
    user_answer = None
    __points = None

    is_right_answer = False

    def __init__(self, question_text, level, answer):
        """Инициализирует экземпляр класса."""
        self.question_text = question_text
        self.level = level
        self.answer = answer
        self.__points = int(self.level) * 10

    def get_points(self):
        """Возвращает int, количество баллов."""
        return self.__points

    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает
        с верным ответом, иначе False.
        """
        if self.user_answer.lower() == self.answer:
            return True
        return False

    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5.
        """
        self.is_asked = True
        return f"Question: {self.question_text}\nLevel: {self.level}/5"

    def build_positive_feedback(self):
        """
        Возвращает:
        Ответ верный, получено __ баллов.
        """
        self.is_right_answer = True
        return f"Well done! You got {self.get_points()} points.\n"

    def build_negative_feedback(self):
        """
        Возвращает:
        Ответ неверный, верный ответ __.
        """
        return f"Wrong! Correct answer: {self.answer}.\n"

    def ask_question(self):
        """Задает вопросы."""
        print(self.build_question())

    def get_answer(self):
        """Проверяет ответы."""
        self.user_answer = input("Enter your answer: ")
        if self.is_correct():
            print(self.build_positive_feedback())
        else:
            print(self.build_negative_feedback())
