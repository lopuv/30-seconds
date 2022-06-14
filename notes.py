import pandas

a = ["answer_a", "answer_b", "answer_c", "answer_d"]
# get csv file and print it to the screen in a prettytable

answers = []

data = pandas.read_csv("question.csv")

answer_a = data[a[0]]
answer_b = data[a[1]]
answer_c = data[a[2]]
answer_d = data[a[3]]

answers.append(answer_a)
answers.append(answer_b)
answers.append(answer_c)
answers.append(answer_d)

for right in answers:
    if data["right_answer"].all() == right.all():
        break

# look first for right position to create the buttons
        answer = ["antwoord A", "antwoord B", "antwoord C", "antwoord D"]
        y = 230
        x = 230
        for a in answer:
            self.btn = Button(self, text=a, bg=self.SETUP["blue_sapphire"], fg=self.SETUP["isabelline"],
                              width=15, height=2)  # command here
            self.btn.place(y=y, x=x)
            y += 100
            x += 100

