import random
from turtle import Turtle, Screen
from typing import Tuple, List
from string import ascii_letters
coach = Turtle()
screen = Screen()
coach.speed(0)
coach.shape('turtle')
width = 1200
baseY = -200


def setup() -> Tuple[str, List[str], List[str]]:
    """
    Initialize the answer for this game of hangman
    As well as the correct and incorrect guesses
    """
    words = ['book', 'video games', 'basketball', 'e-mail', 'hot wings']
    answer = random.choice(words)
    correct = ['_' if letter not in '- \'' else letter for letter in answer]
    wrong_guesses = []
    return (answer, correct, wrong_guesses)


def draw_blanks(ans: str) -> None:
    """
    Draw evenly spaced blanks at the beginning
    Of a game of hangman
    """
    coach.up()
    coach.goto(-width/2, baseY)
    coach.down()
    for letter in ans:
        if letter in '- \'':
            coach.up()
        coach.fd(width/(len(ans) * 2))
        coach.up()
        coach.fd(width/(len(ans) * 2))
        coach.down()
    draw_hanged_man([])


def draw_hanged_man(inc: List[str]) -> None:
    """
    Draw the correct body part of the hanged man
    given the number of incorrect guesses made
    """
    if (num := len(inc)) == 0:
        coach.up()
        coach.goto(-100, 0)
        coach.down()
        coach.seth(90)
        coach.fd(50)
        coach.rt(90)
        coach.fd(200)
        coach.right(90)
        coach.fd(50)
        coach.up()
        coach.goto(-50, 50)
        coach.down()
        coach.seth(90)
        coach.fd(150)
        coach.rt(90)
        coach.fd(100)
        coach.rt(90)
        coach.fd(25)
    elif num == 1:
        coach.seth(0)
        coach.circle(-10, 540)
    elif num == 2:
        coach.left(90)
        coach.fd(25)
        coach.bk(20)
    elif num == 3:
        coach.right(15)
        coach.fd(10)
        coach.bk(10)
    elif num == 4:
        coach.left(30)
        coach.fd(10)
        coach.bk(10)
        coach.right(15)
        coach.fd(20)
    elif num == 5:
        coach.right(25)
        coach.fd(7)
        coach.bk(7)
    else:
        coach.left(50)
        coach.fd(7)
        coach.bk(7)


def take_turn(incorrect, correct, answer):
    letter = screen.textinput('Guess', 'Guess a lettter')
    if letter is None or len(letter) != 1 or letter not in ascii_letters or (
            letter in incorrect or letter in set(correct)):
        print('Invalid Guess')
    elif letter in answer:
        for i, let in enumerate(answer):
            if let == letter:
                correct[i] = letter
        # if it is, we want change it graphically
    else:
        print('Incorrect')
        incorrect.append(letter)
        draw_hanged_man(incorrect)
        # draw a part of the hangman
    return (incorrect, correct)


answer, correct, wrong_guesses = setup()
draw_blanks(answer)
print(answer)
while '_' in correct and len(wrong_guesses) < 6:
    wrong_guesses, correct = take_turn(wrong_guesses, correct, answer)
