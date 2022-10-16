from tkinter import *
from quiz_brain import QuizBrain


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.THEME_COLOR = "#375362"
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=self.THEME_COLOR)
        self.score_label = Label(text=f"Score: {self.score}", pady=20, bg=self.THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, fill="black",
                                                     width=280, text="some text",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20)
        self.true_photo = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=self.true_photo, command=self.yes, highlightthickness=0)
        self.yes_button.grid(column=0, row=2, pady=20)
        self.false_photo = PhotoImage(file="images/false.png")
        self.no_button = Button(image=self.false_photo, command=self.no, highlightthickness=0)
        self.no_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached to the end of quiz.")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def yes(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def no(self):
        is_right = self.quiz.check_answer("no")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
