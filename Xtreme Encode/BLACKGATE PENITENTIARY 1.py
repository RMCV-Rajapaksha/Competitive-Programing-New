# Read number of crew members
n = int(input())

# Dictionary to store crew members by height
crew_dict = {}

for _ in range(n):
    # Read name and height
    name, height = input().split()
    height = int(height)
    
    # Add the name to the corresponding height group
    if height not in crew_dict:
        crew_dict[height] = []
    crew_dict[height].append(name)

# Sort heights and prepare for output
sorted_heights = sorted(crew_dict.keys())

current_position = 1
result = []

for height in sorted_heights:
    # Sort the names alphabetically within the same height group
    crew_dict[height].sort()
    
    # Calculate the min and max position for this group
    min_pos = current_position
    max_pos = current_position + len(crew_dict[height]) - 1
    
    # Create the output string for this group
    result.append(f"{' '.join(crew_dict[height])} {min_pos} {max_pos}")
    
    # Update the current position for the next group
    current_position = max_pos + 1

# Print the final result
for line in result:
    print(line)