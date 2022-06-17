from tkinter import *
from tkinter.ttk import Label
import pandas
import time


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
        self.opt_sel = IntVar()
        self.tekst = "hello"
        self.btn = Button(self, text="Start", bg=self.SETUP["blue_sapphire"], fg=self.SETUP["isabelline"],
                          width=15, height=2, command=lambda *args: self.clear(1))
        self.a = 0
        self.a2 = 0
        self.answer = []
        self.score = 0
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

    def check_answer(self):
        d = self.data["right_answer"][self.a2]
        opt = self.opt_sel.get()

        if int(d) == opt:
            self.score += 10
            self.clear(3)
        else:
            self.score -= 10
            self.clear(4)

        # if print(int(d) == opt):
        #     self.score += 10
        #     self.clear(3)  # right answer
        # else:
        #     self.score -= 10
        #     self.clear(4)  # wrong answer

    def answers(self):
        options = ["answer_a", "answer_b", "answer_c", "answer_d"]
        self.configure(bg=self.SETUP["pewter_blue"])

        for a in range(0, 4):
            answer = self.data[options[a]]
            self.answer.append(answer)

        y = 230
        x = 150
        q_list = []
        t = 0
        for _ in options:
            btn = Radiobutton(self, text=self.answer[self.a][self.a2], bg=self.SETUP["blue_sapphire"],
                              fg=self.SETUP["isabelline"], width=15, height=2, variable=self.opt_sel,
                              value= len(q_list)+1, indicatoron=False, command=self.check_answer)  # adjust this number
            btn.deselect()
            btn.place(y=y, x=x)
            self.a += 1
            t += 1
            q_list.append(btn)
            x -= 150
            if t == 4:
                t = 0
            if x == -150:
                x = 150
                y -= 200
        return q_list
        # check if the answer clicked is equal to the thing that is in the csv file
        # activate the timer
        # have a var that

        # do a self.clear(3) to trigger the right_answer function

    def ref(self):
        self.update()
        time.sleep(5)
        self.a2 += 1
        self.clear(1)

    def right_answer(self):
        self.configure(bg=self.SETUP["green"])
        self.tekst = "Gefeliciteerd de vraag is goed"
        self.lable(tekst=self.tekst, fg_color=self.SETUP["isabelline"],
                   bg_color=self.SETUP["green"], y=200, x=200)
        self.tekst = f"je huidige score is {self.score}"
        self.lable(tekst=self.tekst, fg_color=self.SETUP["isabelline"],
                   bg_color=self.SETUP["green"], y=100, x=100)
        # call to a timer method so it can go to the next question self.a needs a random function so the rest of the
        # answer function will work and conintue the quiz
        self.ref()

    def wrong_answer(self):
        self.configure(bg=self.SETUP["red"])
        self.tekst = "Helaas de vraag is fout volgende keer beter"
        self.lable(tekst=self.tekst, fg_color=self.SETUP["isabelline"],
                   bg_color=self.SETUP["red"], y=200, x=200)
        self.tekst = f"je huidige score is {self.score}"
        self.lable(tekst=self.tekst, fg_color=self.SETUP["isabelline"],
                   bg_color=self.SETUP["red"], y=100, x=100)
        self.ref()
