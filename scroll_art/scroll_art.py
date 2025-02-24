import random, time, os


WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.008

EMPTY_CHAR = ' '
STRUT_CHAR = '🌀'

try:
    strut_points = [(0, True)]  # list of (position, going_right_bool)
    next_strut_point_at = random.randint(1, WIDTH // 2)
    

    while True:
        row = [EMPTY_CHAR] * WIDTH

        # There's a buggy case where somehow strut_points can end up empty. Let's just restart it then:
        if len(strut_points) == 0:
            strut_points = [(0, True)]  # list of (position, going_right_bool)
            next_strut_point_at = random.randint(3, WIDTH // 3)

        # Add a new strut point if it is time
        if strut_points[-1][0] == next_strut_point_at:
            strut_points.append((next_strut_point_at, not strut_points[-1][1]))

            if strut_points[-1][1]:
                # next next_strut_point_at between here and right edge
                if (WIDTH - 1) - next_strut_point_at > (WIDTH // 2):
                    # The distance to the right edge is too far, so let's do somewhere closer
                    next_strut_point_at = random.randint(next_strut_point_at, (WIDTH - 1 - next_strut_point_at) // 2 + next_strut_point_at)
                else:
                    next_strut_point_at = random.randint(next_strut_point_at, WIDTH - 1)
            else:
                # next next_strut_point_at between here and left edge
                if next_strut_point_at - 0 > (WIDTH // 2):
                    # the distance to the left edge is too far, so let's do somewhere closer
                    next_strut_point_at = random.randint(next_strut_point_at // 2, next_strut_point_at)
                else:
                    next_strut_point_at = random.randint(0, next_strut_point_at)

        # Create the row characters
        delete_indexes = []
        for i, (pos, going_right) in enumerate(strut_points):
            row[pos] = STRUT_CHAR

            # Move strut points (or mark them for deletion)
            if pos == WIDTH - 1 and going_right:
                delete_indexes.append(i)
            elif pos == 0 and not going_right:
                delete_indexes.append(i)
            elif going_right:
                strut_points[i] = (pos + 1, True)
            elif not going_right:
                strut_points[i] = (pos - 1, False)
            else:
                assert False

        # Remove strut points that have gone off the sides:
        for i in range(len(delete_indexes) - 1, -1, -1):
            del strut_points[delete_indexes[i]]

        print(''.join(row))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Vertical Struts by Al Sweigart al@inventwithpython.com 2024')

#notes from class:

    # fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# count = 0
# while count < 6:
#     print(count)
#     count += 1 #same as count = count + 1
# import random, os, time

# while True:
#     print("hello")

# i = 0
# while True:
#     print(i)
#     i += 1

# import time

# while True:
#     print(i)
#     i += 1
#     time.sleep(0.1)

# while True:
#     line = '@' * 50
#     print(line)
#     time.sleep(0.1)

# import random, time, os

# while True:
#     line = ''
#     width = os.get_terminal_size()[0] - 1
#     for i in range(width):
#         if random.randint(0, 10) < 5:
#             line += "@"
#         else:
#             line = line + ' '
#     print(line)
#     time.sleep(0.1)

# import random, time, os
# os.system('cls | clear')

# WIDTH = os.get_terminal_size()[0] - 1
# MIN_TRAIL_LEN = 5

# try:
#     while True:
#         trail_length = random.randint(MIN_TRAIL_LEN, WIDTH - 2)
#         for i in range(trail_length):
#             print('_' * i + '🐌', end='', flush=True)
#             time.sleep(0.9 / trail_length)  # Use 0.9 instead of 1.0 because printing adds a delay and I want it to be roughly 1 second per snail.
#             print('\b' * (i + 2), end='', flush=True)
#         print('_' * trail_length + '🐌', end='', flush=True)

#         print('\n' * random.randint(1, 6)) # print new lines between the tails

# except KeyboardInterrupt:
#     print('Snail Trail, by Al Sweigart al@inventwithpython.com 2024')

# __version__ = 0
# import sys, time

# indentSize = 0  # How many spaces to indent.

# try:
#     while True:  # The main program loop.
#         # Zig to the right 20 times:
#         for i in range(20):
#             indentSize = indentSize + 5
#             indentation = ' ' * indentSize
#             print(' ' * indentSize + '********')
#             time.sleep(0.05)  # Pause for 50 milliseconds.

#         # Zag to the left 20 times:
#         for i in range(20):
#             indentSize = indentSize - 5
#             indentation = ' ' * indentSize
#             print(indentation + '********')
#             time.sleep(0.05)  # Pause for 50 milliseconds.
# except KeyboardInterrupt:
#     sys.exit()  # When Ctrl-C is pressed, end the program.

# import math, time, os, sys

# os.system('cls | clear')  # Clear the screen

# width = os.get_terminal_size()[0] - 1
# DELAY = 0.1
# STEP_INCREASE = 0.3

# def main():
#     if len(sys.argv) > 1:
#         message = sys.argv[1]
#     else:
#         message = 'Hello!'

#     step = 0.0
#     while True:  # Main program loop.
#         width = os.get_terminal_size()[0] - 1
#         multiplier = (width - len(message)) / 2
#         sinOfStep = math.sin(step) /5
#         padding = ' ' * int((sinOfStep + 1) * multiplier)
#         print(padding + message)
#         time.sleep(DELAY)
#         step += STEP_INCREASE

# try:
#     main()
# except KeyboardInterrupt:
#     print('Sine Message, by Al Sweigart al@inventwithpython.com 2021')

# import random, math, os, time

# WIDTH = os.get_terminal_size()[0]
# DELAY = 0.05
# THORN_CHAR = '-'

# LEVELS = [1, 1, 1, 1, 1, 1, 1, 3, 6]
# MULTIPLIER = 10

# try:
#     while True:
#         line_length = int(random.choice(LEVELS) * ((random.random() + 1) * MULTIPLIER))
#         line = THORN_CHAR * line_length
        
#         if len(line) > WIDTH:
#             line = THORN_CHAR * WIDTH # if the length exceeds the WIDTH, make it equal to WIDTH 

#         print(line.center(WIDTH)) # align the line in the center of the WIDTH
#         time.sleep(DELAY)
        
# except KeyboardInterrupt:
#     print('Thorns, by Al Sweigart al@inventwithpython.com 2024')

# import random, time, os

# os.system('cls | clear')  # Clear the screen

# # Set up the constants:
# MIN_STREAM_LENGTH = 6  # (!) Try changing this to 1 or 50.
# MAX_STREAM_LENGTH = 14  # (!) Try changing this to 100.
# DELAY = 0.1  # (!) Try changing this to 0.0 or 2.0.
# STREAM_CHARS = ['0', '1']  # (!) Try changing this to other characters.

# # Density can range from 0.0 to 1.0:
# DENSITY = 0.02  # (!) Try changing this to 0.10 or 0.30.


# WIDTH = 79  #os.get_terminal_size()[0] - 1

# # For each column, when the counter is 0, no stream is shown.
# # Otherwise, it acts as a counter for how many times a 1 or 0
# # should be displayed in that column.
# columns = [0] * WIDTH
# try:
#     while True:
#         # Set up the counter for each column:
#         for i in range(WIDTH):
#             if columns[i] == 0:
#                 if random.random() <= DENSITY:
#                     # Restart a stream on this column.
#                     columns[i] = random.randint(MIN_STREAM_LENGTH,
#                                                 MAX_STREAM_LENGTH)

#             # Display an empty space or a 1/0 character.
#             if columns[i] > 0:
#                 print(random.choice(STREAM_CHARS), end='')
#                 columns[i] -= 1
#             else:
#                 print(' ', end='')
#         print()  # Print a newline at the end of the row of columns.
#         time.sleep(DELAY)
# except KeyboardInterrupt:
#     print('Matrix Screensaver, by Al Sweigart al@inventwithpython.com 2021')

# import time, shutil

# WIDTH = shutil.get_terminal_size()[0] - 1
# DELAY = 0.5

# WORM_LENGTH = 3

# STRETCHED_BODY = 'o' + ('o' * (WORM_LENGTH * 2)) + 'o'
# BUNCHED_BODY = 'o' + ('O' * WORM_LENGTH) + 'o'
# indent = 0
# while indent + WORM_LENGTH * 2 + 2 < WIDTH:
#     backspaces_str = "\b" * (indent + WORM_LENGTH * 2 + 2)

#     indentation_str = ' ' * indent
#     print(backspaces_str + indentation_str + STRETCHED_BODY, flush=True, end='')
#     time.sleep(DELAY)

#     indent += WORM_LENGTH

#     indentation_str = ' ' * indent
#     print(backspaces_str + indentation_str + BUNCHED_BODY, flush=True, end='')
#     time.sleep(DELAY)
# print()