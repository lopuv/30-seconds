from tkinter import *
from tkinter.ttk import Label
import pandas


class UI(Tk):

    def __init__(self):
        super().__init__()
        self.SETUP = {
            # window color
            "pewter_blue": "#7EA8BE",
            # button color
            "blue_sapphire": "#28536B",
            # text color
            "isabelline": "#F6F0ED",
            # question wrong
            "red": "#FF0000",
            # question right
            "green": "#90EE90",
            # font style
            "style": "Noto Sans TC"
        }
        self.tekst = "hello"
        self.btn = Button(self, text="Start", bg=self.SETUP["blue_sapphire"], fg=self.SETUP["isabelline"],
                          width=15, height=2, command=lambda *args: self.clear(1))
        self.answer = []
        self.data = pandas.read_csv("question.csv")

        self.mainscreen()

    def lable(self, tekst, fg_color, bg_color, y, x):
        label = Label(self, text=tekst)
        label.place(y=y, x=x)
        label.configure(foreground=fg_color, background=bg_color,
                        font=(self.SETUP["style"], 30))

    def mainscreen(self):
        self.title("30seconds")
        self.geometry("500x500")
        self.configure(bg=self.SETUP["pewter_blue"])
        self.lable(tekst=self.tekst, fg_color=self.SETUP["isabelline"],
                   bg_color=self.SETUP["pewter_blue"], y=200, x=200)
        self.btn.place(y=250, x=250)
        self.mainloop()

    def clear(self, number):
        for widgets in self.winfo_children():
            widgets.destroy()
        if number == 1:
            self.answers()
        elif number == 2:
            self.mainscreen()
        elif number == 3:
            self.right_answer()
        elif number == 4:
            self.wrong_answer()

    def check_answer(self, answer):
        for a in answer:
            if self.data["right_answer"].all() == a.all():
                print(self.data["right_answer"])

    def answers(self):
        # look first for right position to create the buttons
        # answer = ["antwoord A", "antwoord B", "antwoord C", "antwoord D"]
        a = ["answer_a", "answer_b", "answer_c", "answer_d"]

        answer_a = self.data[a[0]]
        answer_b = self.data[a[1]]
        answer_c = self.data[a[2]]
        answer_d = self.data[a[3]]

        self.answer.append(answer_a)
        self.answer.append(answer_b)
        self.answer.append(answer_c)
        self.answer.append(answer_d)

        a = 4
        b = 0
        y = 230
        x = 230
        while a != 0:
            self.btn = Button(self, text=self.answer[b], bg=self.SETUP["blue_sapphire"], fg=self.SETUP["isabelline"],
                              width=15, height=2, command=lambda *args: self.check_answer(self.answer[b]))  # adjust this number
            self.btn.place(y=y, x=x)
            y = 300
            x = 300
            a -= 1
            b += 1
            print(b)
            if x >= 400:
                print(y, x)
                y += -20
                x += -20
        # check if the answer clicked is equal to the thing that is in the csv file
        # activate the timer
        # have a var that

        # do a self.clear(3) to trigger the right_answer function

    def right_answer(self):
        self.configure(bg=self.SETUP["green"])
        self.tekst = "Gefeliciteerd de vraag is goed"
        self.lable(tekst=self.tekst, fg_color=self.SETUP["isabelline"],
                   bg_color=self.SETUP["green"], y=200, x=200)

    def wrong_answer(self):
        self.configure(bg=self.SETUP["red"])
        self.tekst = "Helaas de vraag is fout volgende keer beter"
        self.lable(tekst=self.tekst, fg_color=self.SETUP["isabelline"],
                   bg_color=self.SETUP["red"], y=200, x=200)
