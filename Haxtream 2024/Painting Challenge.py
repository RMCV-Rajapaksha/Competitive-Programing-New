def max_paint_count(P, Q, final_colors):
    # Initialize an array to keep track of the last painter for each cell
    last_painter = [0] * P
    
    # Initialize a dictionary to store the leftmost unpainted cell for each color
    leftmost_unpainted = {color: 0 for color in range(1, Q + 1)}
    
    # Initialize the maximum paint count
    max_count = 0
    
    # Iterate through the cells from left to right
    for i, color in enumerate(final_colors):
        # Find the leftmost cell that needs to be painted with this color
        start = leftmost_unpainted[color]
        
        # Paint all cells from start to i with the current color
        for j in range(start, i + 1):
            if last_painter[j] != color:
                last_painter[j] = color
                max_count = max(max_count, last_painter.count(color))
        
        # Update the leftmost unpainted cell for all colors
        for c in range(1, Q + 1):
            leftmost_unpainted[c] = max(leftmost_unpainted[c], i + 1)
    
    return max_count

# Read input
P, Q = map(int, input().split())
final_colors = list(map(int, input().split()))

# Calculate and print the result
result = max_paint_count(P, Q, final_colors)
print(result)