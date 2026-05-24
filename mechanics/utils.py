"""
This module contains utility functions
"""

import os
import time
import sys

def clear_screen():
    """Clear the console screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')

def clear_lines(n):
    for _ in range(n):
        sys.stdout.write("\033[F") # Move cursor up
        sys.stdout.write("\033[K") # Clear line content
    sys.stdout.flush()

def pause(seconds = 2):
    """Pause the program for a given number of seconds."""
    time.sleep(seconds)

def box(value, valu2= None):
    print("=" * 40)
    # The string inside the '|' symbols will be exactly 38 characters wide and centered
    print(f"|{value:^38}|")
    if valu2:
        print(f"|{valu2:^38}|")
    print("=" * 40)

def line():
    print("="*40)

