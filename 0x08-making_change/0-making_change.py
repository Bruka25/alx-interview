#!/usr/bin/python3

"""Module for determining the number of coins needed to meet a given amount
   total
"""

from collections import deque


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount.

    Returns:
        int: The fewest number of coins needed to meet the total. If the total
             is 0 or less, return 0. If the total cannot be met by any number
             of coins, return -1.
    """
    if total <= 0:
        return 0

    # Use BFS to find the minimum number of coins
    queue = deque([(0, 0)])  # (current_amount, number_of_coins)
    visited = set()

    while queue:
        current_amount, number_of_coins = queue.popleft()

        for coin in coins:
            next_amount = current_amount + coin

            if next_amount == total:
                return number_of_coins + 1
            if next_amount < total and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, number_of_coins + 1))

    return -1
