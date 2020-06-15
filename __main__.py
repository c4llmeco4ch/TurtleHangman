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


def take_turn(incorrect, correct, answer):
    letter = screen.textinput('Guess', 'Guess a lettter')
    if letter is None or len(letter) != 1 or letter not in ascii_letters or (
            letter in incorrect or letter in set(correct)):
        pass
    elif letter in answer:
        for i, let in enumerate(answer):
            if let == letter:
                correct[i] = letter
        # if it is, we want change it graphically
    else:
        incorrect.append(letter)
        # draw a part of the hangman
    return (incorrect, correct)


answer, correct, wrong_guesses = setup()
draw_blanks(answer)
print(answer)
wrong_guesses, correct = take_turn(wrong_guesses, correct, answer)
