from random import choice

questions = ["Why is the sky blue?", "Are we getting there?", "Can I have chocolate?"]
question = choice(questions)

answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why? ").strip().lower()

print("Oh...It makes sense!")


