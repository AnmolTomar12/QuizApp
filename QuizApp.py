import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar

questions = [
    "What is the capital of India?",
    "What is currency of India?",
    "What is the capital of Uttrakhand?",
    "Name the state animal of Uttrakhand?",
    "Total number of national parks in Uttrakhand?"
]

options = [
    ["New York", "Madrid", "Tokyo", "New Delhi"],
    ["Doller", "Rupees", "Dinar", "Pound"],
    ["Haridwar", "Mussoorie", "Dehradun", "Nainital"],
    ["Spotted Deer", "Barasingha", "Musk Deer", "Chinkara"],
    ["6", "5", "3", "7"]
]

answers = [3, 1, 2, 2, 1]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        self.question_index = 0
        self.score = 0
        self.time_left = 10
        self.timer_id = None

        self.start_screen()

    def start_screen(self):
        self.clear_screen()
        self.title_label = tk.Label(self.root, text="Welcome to the Quiz App", font=('Arial', 24, 'bold'), bg="#f0f0f0")
        self.title_label.pack(pady=40)

        self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz, font=('Arial', 16), bg="#4CAF50", fg="white", padx=20, pady=10)
        self.start_button.pack(pady=20)

    def start_quiz(self):
        self.clear_screen()
        self.question_label = tk.Label(self.root, text=questions[self.question_index], font=('Arial', 18, 'bold'), bg="#f0f0f0")
        self.question_label.pack(pady=20)

        self.var = tk.IntVar()

        self.option1 = tk.Radiobutton(self.root, text=options[self.question_index][0], variable=self.var, value=0, font=('Arial', 14), bg="#f0f0f0")
        self.option1.pack(anchor='w', padx=20)

        self.option2 = tk.Radiobutton(self.root, text=options[self.question_index][1], variable=self.var, value=1, font=('Arial', 14), bg="#f0f0f0")
        self.option2.pack(anchor='w', padx=20)

        self.option3 = tk.Radiobutton(self.root, text=options[self.question_index][2], variable=self.var, value=2, font=('Arial', 14), bg="#f0f0f0")
        self.option3.pack(anchor='w', padx=20)

        self.option4 = tk.Radiobutton(self.root, text=options[self.question_index][3], variable=self.var, value=3, font=('Arial', 14), bg="#f0f0f0")
        self.option4.pack(anchor='w', padx=20)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=('Arial', 14), bg="#2196F3", fg="white", padx=20, pady=10)
        self.next_button.pack(pady=20)

        self.progress = Progressbar(self.root, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=10)

        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_left} seconds", font=('Arial', 14), bg="#f0f0f0")
        self.timer_label.pack(pady=10)

        self.start_timer()

    def start_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.time_left = 10
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left} seconds")
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.next_question()

    def next_question(self):
        if self.var.get() == answers[self.question_index]:
            self.score += 1

        self.question_index += 1

        if self.question_index == len(questions):
            self.show_results()
        else:
            self.update_question()

    def update_question(self):
        self.question_label.config(text=questions[self.question_index])
        self.option1.config(text=options[self.question_index][0])
        self.option2.config(text=options[self.question_index][1])
        self.option3.config(text=options[self.question_index][2])
        self.option4.config(text=options[self.question_index][3])
        self.var.set(-1)
        self.progress['value'] = (self.question_index / len(questions)) * 100
        self.start_timer()

    def show_results(self):
        self.clear_screen()
        result_text = f"Your score is {self.score}/{len(questions)}"
        self.result_label = tk.Label(self.root, text=result_text, font=('Arial', 24, 'bold'), bg="#f0f0f0")
        self.result_label.pack(pady=40)

        self.restart_button = tk.Button(self.root, text="Restart Quiz", command=self.restart_quiz, font=('Arial', 16), bg="#4CAF50", fg="white", padx=20, pady=10)
        self.restart_button.pack(pady=20)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, font=('Arial', 16), bg="#f44336", fg="white", padx=20, pady=10)
        self.quit_button.pack(pady=20)

    def restart_quiz(self):
        self.question_index = 0
        self.score = 0
        self.start_quiz()

    def clear_screen(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()