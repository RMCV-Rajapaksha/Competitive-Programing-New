import math

def calculate_thread_length():
    radius = int(input())
    letters = {}
    for _ in range(26):
        letter, angle = input().split()
        letters[letter] = float(angle)

    message = input().upper()
    message = ''.join(filter(str.isalpha, message))

    thread_length = 0
    prev_angle = None
    for letter in message:
        angle = letters[letter]
        if prev_angle is not None:
            thread_length += 2 * radius * math.sin(math.radians(abs(angle - prev_angle)) / 2)
        prev_angle = angle

    thread_length += radius
    print(math.ceil(thread_length))

calculate_thread_length()