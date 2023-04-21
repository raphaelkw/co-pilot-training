# Write unit tests for main.py.

# Path: tests/test_puzzle.py
# Compare this snippet from main.py:

# import main
# import pytest
from main import game


# Define a test case for when the user chooses rock and the computer chooses scissors.
def test_case_rock_scissors():
    # Set the user's choice to rock.
    user_choice = "rock"
    # Set the computer's choice to scissors.
    computer_choice = "scissors"
    # Assert that the user wins.
    assert game(user_choice, computer_choice) == "You win!"


# Define a test case for when the user chooses rock and the computer chooses lizard.
def test_case_rock_lizard():
    # Set the user's choice to rock.
    user_choice = "rock"
    # Set the computer's choice to lizard.
    computer_choice = "lizard"
    # Assert that the user wins.
    assert game(user_choice, computer_choice) == "You win!"


# Define a test case for when the user chooses paper and the computer chooses rock.
def test_case_paper_rock():
    # Set the user's choice to paper.
    user_choice = "paper"
    # Set the computer's choice to rock.
    computer_choice = "rock"
    # Assert that the user wins.
    assert game(user_choice, computer_choice) == "You win!"


# Define a test case for when the user chooses paper and the computer chooses spock.
def test_case_paper_spock():
    # Set the user's choice to paper.
    user_choice = "paper"
    # Set the computer's choice to spock.
    computer_choice = "spock"
    # Assert that the user wins.
    assert game(user_choice, computer_choice) == "You win!"


# Define a test case for when the user chooses scissors and the computer chooses paper.
def test_case_scissors_paper():
    # Set the user's choice to scissors.
    user_choice = "scissors"
    # Set the computer's choice to paper.
    computer_choice = "paper"
    # Assert that the user wins.
    assert game(user_choice, computer_choice) == "You win!"


# Define a test case for when the user chooses scissors and the computer chooses lizard.
def test_case_scissors_lizard():
    # Set the user's choice to scissors.
    user_choice = "scissors"
    # Set the computer's choice to lizard.
    computer_choice = "lizard"
    # Assert that the user wins.
    assert game(user_choice, computer_choice) == "You win!"


# Define a test case for when the user chooses lizard and the computer chooses paper.
def test_case_lizard_paper():
    # Set the user's choice to lizard.
    user_choice = "lizard"
    # Set the computer's choice to paper.
    computer_choice = "paper"
    # Assert that the user wins.
    assert game(user_choice, computer_choice) == "You win!"