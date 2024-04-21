def new_game():
    num_answers=1
    right_answers=0
    input_letter = []
    for quest,value in questions.items():
        print("----------------------------")
        print("----------------------------")
        print(quest)
        for answer in options[num_answers-1]:
            print(answer)
        print("----------------------------")
        num_answers +=1
        lette=input("Enter the answer! ").upper()
        input_letter.append(lette)
        right_answers+=check_answer(lette,value)
    print(input_letter)
    print(f"You have {right_answers} right answers of {len(questions)} questions")
def check_answer(entered_letter, correct_answer):
    if entered_letter==correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0
def display_score():
    pass
def play_again():
    pl_ag = input("Do you want to play again? yes or no ")
    if pl_ag=="no":
        return False
    else:
        return True


questions = {
    "Who created Python? ": "A",
    "What year was python created? ": "B",
    "Python is tributed to which comeedy group? ": "C",
    "Is the Earth round?": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C: Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What is Earth?"]
           ]

new_game()
while play_again():
    new_game()