#!/usr/bin/python3
"""
This module defines the isWinner function to determine the winner of
a game where Maria and Ben take turns picking prime numbers and removing
them and their multiples from a set of consecutive integers.
"""


def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of the prime number game.

    Args:
        x (int): The number of rounds to be played.
        nums (list): A list of integers where each element is the upper
                     limit of the set of consecutive integers for each round.

    Returns:
        str: The name of the player that won the most rounds, or None if
             there is a tie.
    """
    Ben = 0
    Maria = 0

    for round in range(x):
        playing_numbers = [num for num in range(2, nums[round] + 1)]
        index = 0
        # Sieve prime numbers per round
        while (index < len(playing_numbers)):
            current_prime = playing_numbers[index]
            sieve_index = index + current_prime
            while(sieve_index < len(playing_numbers)):
                playing_numbers.pop(sieve_index)
                sieve_index += current_prime - 1
            index += 1
        # Determine winner - if number of primes is even player 1 wins
        # else player 2 wins. Player 2  also wins if there is only one
        # number to pick from
        prime_count = (len(playing_numbers))
        if prime_count and prime_count % 2:
            Maria += 1
        else:
            Ben += 1

    if Ben == Maria:
        return None
    return 'Ben' if Ben > Maria else 'Maria'
