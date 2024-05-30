import tkinter as tk
from tkinter import messagebox

# Список запитань для різних рівнів
questions = {
    'Легкий': [
        {"question": "Яке слово є прикметником?", "options": ["Веселий", "Бігати", "Дерево"], "answer": "Веселий"},
        {"question": "Яке слово є іменником?", "options": ["Читати", "Книга", "Швидкий"], "answer": "Книга"},
        {"question": "Яке слово є дієсловом?", "options": ["Писати", "Малий", "Столик"], "answer": "Писати"}
    ],
    'Середній': [
        {"question": "Яке з цих слів має корінь 'ліс'?", "options": ["Лісник", "Сіль", "Лисиця"], "answer": "Лісник"},
        {"question": "Яке з цих слів є збірним іменником?", "options": ["Клас", "Столик", "Вчитель"], "answer": "Клас"},
        {"question": "Яке з цих слів має префікс 'пере'?", "options": ["Переклад", "Легко", "Твердий"],
         "answer": "Переклад"}
    ],
    'Складний': [
        {"question": "Яке з цих слів є прийменником?", "options": ["З-за", "Швидко", "Творчість"], "answer": "З-за"},
        {"question": "Яке з цих слів є дієприкметником?", "options": ["Читаючий", "Книга", "Розумний"],
         "answer": "Читаючий"},
        {"question": "Яке з цих слів має суфікс 'еньк'?", "options": ["Маленький", "Широкий", "Високий"],
         "answer": "Маленький"}
    ]
}

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LinkUthink - Програма для вивчення Української мови")

        # Головний екран
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.welcome_label = tk.Label(self.main_frame, text="Програма для вивчення Української мови",
                                      font=('Helvetica', 16, 'bold'))
        self.welcome_label.pack(pady=20)

        self.app_name_label = tk.Label(self.main_frame, text="LinkUthink", font=('Helvetica', 14, 'italic'))
        self.app_name_label.pack(pady=10)

        self.select_level_label = tk.Label(self.main_frame, text="Виберіть рівень складності", font=('Helvetica', 12))
        self.select_level_label.pack(pady=5)

        self.level_buttons = []
        for level in ['Легкий', 'Середній', 'Складний']:
            button = tk.Button(self.main_frame, text=level, font=('Helvetica', 12),
                               command=lambda lvl=level: self.start_quiz(lvl))
            button.pack(pady=5)
            self.level_buttons.append(button)

        # Кадр для запитань
        self.question_frame = tk.Frame(self.root)

        # Кадр для результатів
        self.result_frame = tk.Frame(self.root)

    def start_quiz(self, level):
        self.main_frame.pack_forget()
        self.question_frame.pack()

        self.level = level
        self.questions = questions[level]
        self.current_question = 0
        self.correct_answers = 0

        self.show_question()

    def show_question(self):
        for widget in self.question_frame.winfo_children():
            widget.destroy()

        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            question_label = tk.Label(self.question_frame, text=q["question"], font=('Helvetica', 14))
            question_label.pack(pady=10)

            self.option_buttons = []
            for option in q["options"]:
                button = tk.Button(self.question_frame, text=option, font=('Helvetica', 12),
                                   command=lambda opt=option: self.check_answer(opt))
                button.pack(pady=5)
                self.option_buttons.append(button)
        else:
            self.show_results()

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_option == correct_answer:
            self.correct_answers += 1
        self.current_question += 1
        self.show_question()

    def show_results(self):
        self.question_frame.pack_forget()
        self.result_frame.pack()

        result_label = tk.Label(self.result_frame,
                                text=f"Ваш результат: {self.correct_answers} з {len(self.questions)}",
                                font=('Helvetica', 14))
        result_label.pack(pady=20)

        restart_button = tk.Button(self.result_frame, text="Пройти тест заново", font=('Helvetica', 12),
                                   command=self.restart_quiz)
        restart_button.pack(pady=10)

        exit_button = tk.Button(self.result_frame, text="Вийти з програми", font=('Helvetica', 12),
                                command=self.root.quit)
        exit_button.pack(pady=10)

    def restart_quiz(self):
        self.result_frame.pack_forget()
        self.main_frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()
