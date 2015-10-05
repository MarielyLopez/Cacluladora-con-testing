import os
import sys

def clear():
    """Cleans the data on screen."""
    if os.name == "posix":
        os.system("reset")
    elif os.name == ("nt"):
        os.system("cls")

def menu_general():
    print_menu()
    answer_menu()

def print_menu():
    clear()
    print "Welcome to my Calculator XD!"
    print "Enter number 1 if you want sum."
    print "Enter number 2 if you want subtract."
    print "Enter number 3 if you want multiply."
    print "Enter number 4 if you want divide."
    print "Enter number 5 if you want exit."


def enter_of_answers():
    answer_one = insert_number()
    answer_two = insert_number()
    print "The answer is:"
    return answer_one, answer_two


def insert_number():
    while True:
        answer = raw_input("Enter a number: ")
        try:
            answer = int(answer)
            return answer
            break
        except Exception:
            print "Try again."


def question_y_n():
    yesornot = True
    while yesornot == True:
        user_answer = raw_input("Do you want make other operation? y / n: ")
        if user_answer == "y" or user_answer == "yes":
            menu_general()
        elif user_answer == "n" or user_answer == "not":
            print " We hope have helped."
            sys.exit(1)
        else:
            print "Insert yes or not."


def answer_menu():
    answer = insert_number()
    answermenu = True
    while answermenu == True:
        if answer == 1:
            print "Go we sum! XD"
            print str(sum(enter_of_answers()))
            question_y_n()
        elif answer == 2:
            print "Go we subtract! XD"
            print str(subtract(enter_of_answers()))
            question_y_n()
        elif answer == 3:
            print "Go we multiply! XD"
            print str(multiply(enter_of_answers()))
            question_y_n()
        elif answer == 4:
            print "Go we divide! XD"
            print str(divide(enter_of_answers()))
            question_y_n()
        elif answer == 5:
            print "We hope have helped."
            sys.exit(1)
        else:
            menu_general()

def sum(numbers):
    return numbers[0] + numbers[1]

def subtract(numbers):
    return numbers[0] - numbers[1]

def multiply(numbers):
    return numbers[0] * numbers[1]

def divide(numbers):
    return numbers[0] / numbers[1]


if __name__ == '__main__':
    menu_general()

