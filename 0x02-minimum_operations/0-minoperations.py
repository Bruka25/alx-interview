#!/usr/bin/env python3

"""MOdule for calculating minimum operations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to have exactly `n` characters 'H' in a file
    using only the operations "Copy All" and "Paste".

    Args:
    - n (int): The number of 'H' characters desired in the file.

    Returns:
    - int: The minimum number of operations required. Returns 0 if `n` is impossible to achieve.

    Explanation:
    - The function uses dynamic programming to build up the minimum operations required for each count of 'H's.
    - Starts with the base case of 1 'H' (0 operations).
    - For each subsequent count from 2 to `n`, computes the minimum operations by considering all possible ways to achieve
      that count using previously computed results.

    Example:
    >>> minOperations(9)
    6
    This returns 6 because the minimum operations to achieve 9 'H's is demonstrated in the example provided:
    H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            ops_count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return ops_count
