from tkinter import *
from tkinter.ttk import Combobox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.quiz_length = len(quiz_brain.question_list)

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0, borderwidth=0)

        """Score label"""
        self.score_label = Label(text=f"Score: 0 of {self.quiz_length}", fg="White", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=1, padx=20, pady=20, sticky="e")

        """Question board"""
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Some question",
            font=("arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        """True button"""
        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            self.window,
            image=self.true_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.selected_answer(user_answer="True")
        )
        self.true_button.grid(column=0, row=3, padx=20, pady=20, sticky="w")

        """False button"""
        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            self.window,
            image=self.false_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.selected_answer(user_answer="False")
        )
        self.false_button.grid(column=1, row=3, padx=20, pady=20, sticky="e")

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def selected_answer(self, user_answer: str):
        is_correct = self.quiz.check_answer(user_answer)
        if is_correct:
            self.canvas.config(background="green")
            self.score_label.config(text=f"Score: {self.quiz.score} of {self.quiz_length}")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)

