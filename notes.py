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
        print(right)



