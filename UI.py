from tkinter import *
from tkinter.ttk import Label


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
        self.mainscreen()

    def lable(self, tekst):
        self.lab = Label(self, text=self.tekst)

    def mainscreen(self):
        global lab
        self.title("30seconds")
        self.geometry("500x500")
        self.configure(bg=self.SETUP["pewter_blue"])
        self.lable(self.tekst)
        self.lab.place(y=200, x=200)
        # font(lettertype, groote)
        # alter font size of the button
        self.lab.configure(foreground=self.SETUP["isabelline"], background=self.SETUP["pewter_blue"],
                             font=(self.SETUP["style"], 30))
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

    def answers(self):
        # look first for right position to create the buttons
        answer = ["antwoord A", "antwoord B", "antwoord C", "antwoord D"]
        y = 230
        x = 230
        for a in answer:
            self.btn = Button(self, text=a, bg=self.SETUP["blue_sapphire"], fg=self.SETUP["isabelline"],
                              width=15, height=2, command=lambda *args: self.clear(3))  # adjust this number
            self.btn.place(y=y, x=x)
            y = 300
            x = 300
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
        self.lable(self.tekst)
        self.lab.place(y=200, x=200)
        self.lab.configure(foreground=self.SETUP["isabelline"], background=self.SETUP["green"],
                           font=(self.SETUP["style"], 30))

    def wrong_answer(self):
        self.configure(bg=self.SETUP["red"])
        self.tekst = "Helaas de vraag is fout volgende keer beter"
        self.lable(self.tekst)
        self.lab.place(y=200, x=200)
        self.lab.configure(foreground=self.SETUP["isabelline"], background=self.SETUP["red"],
                           font=(self.SETUP["style"], 30))