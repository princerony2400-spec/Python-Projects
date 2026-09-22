import subprocess as sp
import time


# Introduction user name

user_name = input("What's your name?\nName :- ")

money = 100


def greet(func):
    def modify():
        print(
            f"Dear {user_name} is Playing...\n"
            "_______-----_______\n"
            f"You have Total {money}$."
        )

        func()

        print("\n")
        print("\n")
        print("\n")
        print("Nice playing ...")

    return modify


#       Question set 1 is here

queshion_1 = [
    "What is the capital of Bangladesh?",
    "How many days are there in a week?",
    "What is 5 + 5?",
    "Which planet is known as the Red Planet?",
    "What color do you get by mixing red and white?",
    "How many months are there in a year?",
    "What is the opposite of hot?",
    "Which animal is called the king of the jungle?",
    "What is 10 - 4?",
    "Which language is mainly used to make web pages?"
]

option_1 = [
    ["Dhaka", "Chittagong", "Sylhet", "Rajshahi"],
    ["Five", "Six", "Seven", "Eight"],
    ["8", "10", "12", "15"],
    ["Earth", "Mars", "Jupiter", "Venus"],
    ["Green", "Purple", "Pink", "Orange"],
    ["10", "11", "12", "13"],
    ["Cold", "Big", "Fast", "Dark"],
    ["Tiger", "Lion", "Elephant", "Bear"],
    ["4", "5", "6", "7"],
    ["HTML", "Python", "C", "Java"]
]

ans_1 = [
    "A",
    "C",
    "B",
    "B",
    "C",
    "C",
    "A",
    "B",
    "C",
    "A"
]


#       Question set 2

queshion_2 = [
    "What is the largest ocean in the world?",
    "How many hours are there in one day?",
    "What is 7 + 8?",
    "Which gas do humans need to breathe?",
    "What is the first month of the year?",
    "Which shape has three sides?",
    "What is 20 divided by 4?",
    "Which country is famous for the Eiffel Tower?",
    "What is the color of the sky on a clear day?",
    "Which device is used to type on a computer?"
]

option_2 = [
    ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
    ["12", "18", "24", "30"],
    ["13", "14", "15", "16"],
    ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
    ["March", "January", "June", "December"],
    ["Square", "Circle", "Triangle", "Rectangle"],
    ["4", "5", "6", "7"],
    ["Italy", "France", "Germany", "Spain"],
    ["Blue", "Green", "Red", "Black"],
    ["Mouse", "Monitor", "Keyboard", "Speaker"]
]

ans_2 = [
    "C",
    "C",
    "C",
    "B",
    "B",
    "C",
    "B",
    "B",
    "A",
    "C"
]


#       Question set 3

queshion_3 = [
    "What is the largest planet in our solar system?",
    "What is 9 multiplied by 3?",
    "Which organ pumps blood in the human body?",
    "How many letters are there in the English alphabet?",
    "Which animal can fly?",
    "What is the opposite of easy?",
    "Which country is known as the Land of the Rising Sun?",
    "What is 100 divided by 10?",
    "Which one is a programming language?",
    "What do plants need to make food?"
]

option_3 = [
    ["Earth", "Mars", "Jupiter", "Saturn"],
    ["18", "21", "27", "30"],
    ["Brain", "Heart", "Lung", "Kidney"],
    ["24", "25", "26", "27"],
    ["Dog", "Cat", "Eagle", "Horse"],
    ["Hard", "Small", "Slow", "Short"],
    ["China", "Japan", "India", "Korea"],
    ["5", "10", "20", "25"],
    ["HTML", "Python", "HTTP", "CSS"],
    ["Moonlight", "Sunlight", "Darkness", "Sand"]
]

ans_3 = [
    "C",
    "C",
    "B",
    "C",
    "C",
    "A",
    "B",
    "B",
    "B",
    "B"
]


speech = "0.8"

print(
    "This program has 3 question sets.\n"
    "Please type (1-3) any one digit"
)

choice = int(input("Type :- "))

print("Loading...")
time.sleep(2)


if choice < 1 or choice > 3:
    print("Fault choice")

else:

    @greet
    def game_start():

        global money

        print("Your question is ...")
        time.sleep(1)

        # ---------------- SET 1 ----------------

        if choice == 1:

            for i in range(len(queshion_1)):

                say = sp.run(
                    [
                        "termux-tts-speak","-r",speech,
                        f"{queshion_1[i]}"
                    ],
                    capture_output=True,
                    check=True,
                    text=True
                )

                print(f"*:- {queshion_1[i]}")
                print(say.stdout.strip())

                time.sleep(1)

                j = option_1[i]

                say_op = sp.run(
                    [
                        "termux-tts-speak"
                        ,"-r",speech,
                        f"Option A is {j[0]}, "
                        f"option B is {j[1]}, "
                        f"option C is {j[2]}, "
                        f"and option D is {j[3]}. "
                        f"Now type your answer"
                    ],
                    capture_output=True,
                    text=True,
                    check=True
                )

                print(
                    f"A :- {j[0]}     -:-     B :- {j[1]}\n"
                    f"C :- {j[2]}     -:-     D :- {j[3]}"
                )

                print(say_op.stdout.strip())

                ans = input("Your Choice :- ").upper()

                time.sleep(1)

                if ans == ans_1[i]:

                    win = sp.run(
                        [
                            "termux-tts-speak"
                            ,"-r",speech,
                            "Correct Answer, Your money is double"
                        ],
                        capture_output=True,
                        check=True,
                        text=True
                    )

                    print(win.stdout.strip())
                    print("Correct answer")

                    money *= 2
                    print (f"Your money is {money}$ ")

                else:

                    print("Wrong Answer")

        # ---------------- SET 2 ----------------

        elif choice == 2:

            for i in range(len(queshion_2)):

                say = sp.run(
                    [
                        "termux-tts-speak",
                        "-r",speech,
                        f"{queshion_2[i]}"
                    ],
                    capture_output=True,
                    check=True,
                    text=True
                )

                print(f"*:- {queshion_2[i]}")
                print(say.stdout.strip())

                time.sleep(1)

                j = option_2[i]

                say_op = sp.run(
                    [
                        "termux-tts-speak",
                        "-r",speech,
                        f"Option A is {j[0]}, "
                        f"option B is {j[1]}, "
                        f"option C is {j[2]}, "
                        f"and option D is {j[3]}. "
                        f"Now type your answer"
                    ],
                    capture_output=True,
                    text=True,
                    check=True
                )

                print(
                    f"A :- {j[0]}     -:-     B :- {j[1]}\n"
                    f"C :- {j[2]}     -:-     D :- {j[3]}"
                )

                print(say_op.stdout.strip())

                ans = input("Your Choice :- ").upper()

                time.sleep(1)

                if ans == ans_2[i]:

                    win = sp.run(
                        [
                            "termux-tts-speak"
                            ,"-r",speech,
                            "Correct Answer, Your money is double"
                        ],
                        capture_output=True,
                        check=True,
                        text=True
                    )

                    print(win.stdout.strip())
                    print("Correct answer")

                    money *= 2
                    print (f"Your money is {money}$ ")

                else:

                    print("Wrong Answer")

        # ---------------- SET 3 ----------------

        elif choice == 3:

            for i in range(len(queshion_3)):

                say = sp.run(
                    [
                        "termux-tts-speak"
                        ,"-r",speech,
                        f"{queshion_3[i]}"
                    ],
                    capture_output=True,
                    check=True,
                    text=True
                )

                print(f"*:- {queshion_3[i]}")
                print(say.stdout.strip())

                time.sleep(1)

                j = option_3[i]

                say_op = sp.run(
                    [
                        "termux-tts-speak"
                        ,"-r",speech,
                        f"Option A is {j[0]}, "
                        f"option B is {j[1]}, "
                        f"option C is {j[2]}, "
                        f"and option D is {j[3]}. "
                        f"Now type your answer"
                    ],
                    capture_output=True,
                    text=True,
                    check=True
                )

                print(
                    f"A :- {j[0]}     -:-     B :- {j[1]}\n"
                    f"C :- {j[2]}     -:-     D :- {j[3]}"
                )

                print(say_op.stdout.strip())

                ans = input("Your Choice :- ").upper()

                time.sleep(1)

                if ans == ans_3[i]:

                    win = sp.run(
                        [
                            "termux-tts-speak"
                            ,"-r",speech,
                            "Correct Answer, Your money is double"
                        ],
                        capture_output=True,
                        check=True,
                        text=True
                    )

                    print(win.stdout.strip())
                    print("Correct answer")
                    

                    money *= 2
                    print(f"Your money is {money}$")

                else:

                    print("Wrong Answer")


    game_start()

