from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.ui_score = Label(text="",
                              bg=THEME_COLOR,
                              fg="white",
                              font=("Arial", 15, "italic"))
        self.ui_score.grid(row=0, column=1)

        true_btn_png = PhotoImage(file="resources/true.png")
        self.true_btn = Button(image=true_btn_png, bg=THEME_COLOR, highlightthickness=0, command=self.click_true_btn)
        self.true_btn.grid(row=2, column=0)

        false_btn_png = PhotoImage(file="resources/false.png")
        self.false_btn = Button(image=false_btn_png, bg=THEME_COLOR, highlightthickness=0, command=self.click_false_btn)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.ui_score.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the test!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def click_true_btn(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false_btn(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
