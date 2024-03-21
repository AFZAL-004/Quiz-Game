questions = ("Jimmy's father has three sons- Paul I and Paul II. Can you guess the name of the third son? ",
             "You're 4th place right now in a race. What place will you be in when you pass the person in 3rd place?",
             "How does a computer get drunk? ",
             "What do you call a fish with no eyes?",
             " How does a programmer flirt?")

options = (("A.Paul III ","B.Jerin","C.Jimmy","D.None"),
           ("A.2nd","B.3rd","C.1st","D.None of the above"),
           ("A. By downloading too much beer.","B.By being infected with a virus ","C.By drinking too much Java","D.By crashing the RAM"),
           ("A.Fsh","B.Blind fish","C.see through fish","D.No-eye-dea"),
           ("A. By saying, You complete me();","B.By asking, Are you an API? Because you've got my endpoints tingling.","C. By offering to debug their code","D.By saying, You're my favorite exception."))

answers = ("C","B","C","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter an option: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"Correct answer is {answers[question_num]}")
    question_num += 1

print("-----------------")
print("Results")
print("-----------------")

print("Answers:",end = "")
for answer in answers:
    print(answer,end="")
print()

print("Guesses: ",end="")
for guess in guesses:
    print(guess,end="")
print()

score = int(score/len(questions)*100)
print(f"Your Score is {score}%")

