#!/usr/bin/python3


"""Module for log parsing"""

import sys
import signal
import re

# Initialize metrics
total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

# Define regex pattern for matching the input format
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>[^\]]+)\] "GET /projects/260 '
    r'HTTP/1.1" (?P<status_code>\d{3}) (?P<file_size>\d+)'
)


def print_statistics():
    """
    Print the current statistics:
    - Total file size.
    - Number of lines for each status code that has occurred.
    """
    global total_file_size, status_code_counts
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """
    Handle the signal interruption (e.g., CTRL + C).
    Print the current statistics and exit the program.

    Args:
        sig (int): Signal number.
        frame (FrameType): Current stack frame.
    """
    print_statistics()
    sys.exit(0)


# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            data = match.groupdict()
            status_code = int(data['status_code'])
            file_size = int(data['file_size'])

            # Update the total file size
            total_file_size += file_size
            # Update the count for the specific status code
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
