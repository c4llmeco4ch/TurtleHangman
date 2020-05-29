import random
from turtle import Turtle
from typing import Tuple, List
coach = Turtle()
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


answer, correct, wrong_guesses = setup()
draw_blanks(answer)
print(answer)
