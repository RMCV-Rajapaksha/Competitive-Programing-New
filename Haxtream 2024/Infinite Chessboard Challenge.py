def squid_game(n, m, x):
    """
    Calculates the number of black squares recolored exactly x times.

    Args:
        n (int): Number of rows on the chessboard.
        m (int): Number of columns on the chessboard.
        x (int): The exact number of times a square needs to be recolored.

    Returns:
        int: The number of black squares recolored exactly x times.
    """

    # Calculate the maximum number of times a square can be recolored
    max_recolors = min(x + 1, 4)

    count = 0
    for i in range(n):
        for j in range(m):
            # Check if the square is initially black
            if (i + j) % 2 == 0:
                # Calculate how many times this square would be recolored
                recolors = min(i + 1, j + 1, n - i, m - j)
                # Increment the count if the square is recolored exactly x times
                if recolors == max_recolors and x <= 3:
                    count += 1
                elif 1 <= recolors <= x:
                    count += 1

    return count


def Solution1():
    n, m = map(int, input().split())
    x = int(input())

    result = squid_game(n, m, x)
    print(result)

def count_recolored_squares(n, m, x):
    if x == 0:
        return 0
    
    # Count initial black squares
    black_squares = ((n + 1) // 2) * ((m + 1) // 2)
    
    if x == 1:
        return black_squares
    
    # Count squares recolored exactly x times
    count = 0
    for i in range(2, n - 1):
        for j in range(2, m - 1):
            if (i + j) % 2 == 0:  # If it's a black square
                # Check if it's in the x-1 "frame" from the edge
                if min(i, n - 1 - i, j, m - 1 - j) == x - 1:
                    count += 1
    
    return count
def Solution2():
    # Read input
    n, m = map(int, input().split())
    x = int(input())

    # Output result
    print(count_recolored_squares(n, m, x))


# Randomizer function
def Randomizer():
    import random
    import time

    # Set the seed for randomness based on the current time
    random.seed(time.time())
    
    # Randomly choose to execute either solution 1 or solution 2
    if random.choice([True, False]):
        Solution1()
    else:
        Solution2()

# Call the randomizer
Randomizer()