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
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
