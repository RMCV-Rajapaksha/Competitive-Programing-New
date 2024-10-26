def create_maze_path(input_string):
    # Step 1: Calculate the number of nodes based on the length of the input string
    num_nodes = min(2 * len(input_string), 100)  # Limit the number of nodes for safety
    start_node = 1  # Define the starting node
    end_node = num_nodes  # Set the end node far from the start to create a path
    
    # Step 2: Generate the binary tree structure with left and right child nodes
    maze_structure = []
    for node in range(1, num_nodes + 1):
        left_child = 2 * node if 2 * node <= num_nodes else 0
        right_child = 2 * node + 1 if 2 * node + 1 <= num_nodes else 0
        maze_structure.append((left_child, right_child))
    
    # Step 3: Output the maze configuration
    print(num_nodes, start_node, end_node)
    for left, right in maze_structure:
        print(left, right)

# Sample input
input_string = input().strip()
create_maze_path(input_string)
