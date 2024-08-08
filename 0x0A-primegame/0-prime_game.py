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

    def is_prime(num):
        """
        Checks if a given number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, otherwise False.
        """
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def sieve(n):
        """
        Uses the Sieve of Eratosthenes to find all prime numbers up to n.

        Args:
            n (int): The upper limit for finding primes.

        Returns:
            list: A list of all prime numbers up to and including n.
        """
        primes = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n + 1) if primes[p]]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        primes = sieve(n)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
