#!/usr/bin/python3

"""Module for determining the number of coins needed to meet a given amount
   total
"""


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

    # Initialize an array to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each amount up to the total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
