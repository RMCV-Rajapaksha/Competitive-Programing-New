# def max_paint_count(P, Q, final_colors):
#     # Initialize an array to keep track of the last painter for each cell
#     last_painter = [0] * P
    
#     # Initialize a dictionary to store the leftmost unpainted cell for each color
#     leftmost_unpainted = {color: 0 for color in range(1, Q + 1)}
    
#     # Initialize the maximum paint count
#     max_count = 0
    
#     # Iterate through the cells from left to right
#     for i, color in enumerate(final_colors):
#         # Find the leftmost cell that needs to be painted with this color
#         start = leftmost_unpainted[color]
        
#         # Paint all cells from start to i with the current color
#         for j in range(start, i + 1):
#             if last_painter[j] != color:
#                 last_painter[j] = color
#                 max_count = max(max_count, last_painter.count(color))
        
#         # Update the leftmost unpainted cell for all colors
#         for c in range(1, Q + 1):
#             leftmost_unpainted[c] = max(leftmost_unpainted[c], i + 1)
    
#     return max_count

# # Read input
# P, Q = map(int, input().split())
# final_colors = list(map(int, input().split()))

# # Calculate and print the result
# result = max_paint_count(P, Q, final_colors)
# print(result)

def max_paint_cost(P, Q, final_colors):
    # Array to store how many times each cell has been painted
    paint_count = [0] * P
    
    # Keep track of whether we've processed this color
    current_colors = final_colors[:]
    
    # Process each contestant's color from 1 to Q
    for color in range(1, Q + 1):
        start = -1
        # Find the largest contiguous subarray that could have been painted with this color
        for i in range(P):
            if current_colors[i] == color:
                if start == -1:
                    start = i
            else:
                if start != -1:
                    # We've found a segment, mark all cells as painted
                    for j in range(start, i):
                        paint_count[j] += 1
                    start = -1
        if start != -1:
            # Handle the case when the segment goes till the end
            for j in range(start, P):
                paint_count[j] += 1
    
    # The result is the maximum paint count of any cell
    return max(paint_count)

# Read input
P, Q = map(int, input().split())
final_colors = list(map(int, input().split()))

# Compute and print the result
print(max_paint_cost(P, Q, final_colors))
