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
            "green": "90EE90",
            # font style
            "style" : "Noto Sans TC"
        }
        self.mainscreen()

    def mainscreen(self):
        self.title("30seconds")
        self.geometry("500x500")
        self.configure(bg=self.SETUP["pewter_blue"])
        self.btn = Button(self, text="Start", bg=self.SETUP["blue_sapphire"], fg=self.SETUP["isabelline"],
                          width=15, height=2, command=lambda *args: self.clear(1))
        self.label = Label(self, text="hello")
        self.label.place(y=200, x=200)
        # font(lettertype, groote)
        # alter font size of the button
        self.label.configure(foreground=self.SETUP["isabelline"], background=self.SETUP["pewter_blue"],
                             font=(self.SETUP["style"], 30))
        self.btn.place(y=250, x=250)
        self.mainloop()

    def clear(self, number):
        for widgets in self.winfo_children():
            widgets.destroy()
        if number == 1:
            self.answers()
        else:
            self.mainscreen()

    def answers(self):
        # look first for right position to create the buttons
        answer = ["antwoord A", "antwoord B", "antwoord C", "antwoord D"]
        y = 230
        x = 230
        for a in answer:
            self.btn = Button(self, text=a, bg=self.SETUP["blue_sapphire"], fg=self.SETUP["isabelline"],
                              width=15, height=2, command=lambda *args: self.clear(0))
            self.btn.place(y=y, x=x)
            y += 100
            x += 100
        # check if the answer clicked is equal to the thing that is in the csv file
        # activate the timer
        # have a var that


