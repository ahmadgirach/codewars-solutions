"""
https://www.codewars.com/kata/5672a98bdbdd995fad00000f

Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper')     // Player 1 won!
rps('scissors','rock')      // Player 2 won!
rps('paper','paper')        // Draw!
"""

from random import choice


ROCK = "rock"
PAPER = "paper"
SCISSOR = "scissor"

OPTIONS = (ROCK, PAPER, SCISSOR)


def is_draw(player1_choice: str, player2_choice: str) -> bool:
    return player1_choice == player2_choice


def rps(player1_choice: str, player2_choice: str) -> str:
    PLAYER_1_WINNING_POSITIONS = ("pr", "sp", "rs")
    PLAYER_2_WINNING_POSITIONS = ("rp", "ps", "sr")

    player1_choice = player1_choice.lower()[0]
    player2_choice = player2_choice.lower()[0]

    combined_choice = player1_choice + player2_choice

    if is_draw(player1_choice, player2_choice):
        result = "Draw"
    elif combined_choice in PLAYER_1_WINNING_POSITIONS:
        result = "Player 1 Won!"
    else:
        result = "Player 2 Won!"

    return result


choice_1 = choice(OPTIONS)
choice_2 = choice(OPTIONS)
print(choice_1, "=>", choice_2)
print(rps(choice_1, choice_2))
