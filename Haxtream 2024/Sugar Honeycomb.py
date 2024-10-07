def find_shape(matrix):
    # Define the templates for each shape
    circle = [
        "00100",
        "01110",
        "11111",
        "01110",
        "00100",

    ]
    
    triangle = [
        "00000",
        "00100",
        "01110",
        "11111",
        "00000",
    ]
    
    star = [
        "00100",
        "00100",
        "11111",
        "00100",
        "00100",
    ]
    
    umbrella = [
        "00100",
        "01110",
        "11111",
        "00100",
        "00100",
    ]
    
    for shape in [circle, triangle, star, umbrella]:
        shape_str = "\n".join(shape)
        if shape_str in matrix:
            return shape[0][0]  # Return the first letter of the shape
    return "-1"

def Solution1():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    # Check if there's at least one test case
    if not data or len(data) < 1:
        return
    
    C = int(data[0])  # Number of test cases
    results = []
    
    index = 1
    for _ in range(C):
        if index >= len(data):
            results.append("-1")
            continue
        
        N = int(data[index])  # Row length of the matrix
        index += 1
        
        # Ensure we read the correct number of rows for the current test case
        if index + N > len(data):
            results.append("-1")
            break
        
        binary_array = "".join(data[index:index + N])
        index += N
        
        shape = find_shape(binary_array)
        results.append(shape)
    
    print(" ".join(results))

def detect_shape(matrix, N):
    # Define templates for each shape
    templates = {
        'C': [
            "0000000",
            "0011100",
            "0111110",
            "0111110",
            "0111110",
            "0011100",
            "0000000"
        ],
        'T': [
            "000000",
            "001000",
            "011100",
            "111110",
            "000000",
            "000000"
        ],
        'S': [
            "0000000",
            "0011100",
            "0111110",
            "1111111",
            "0111110",
            "0011100",
            "0000000"
        ],
        'U': [
            "0000000",
            "0111110",
            "0111110",
            "0111110",
            "0111110",
            "0011100",
            "0000000"
        ]
    }
    
    # Convert the matrix to a list of strings
    matrix_str = ["".join(map(str, row)) for row in matrix]
    
    def matches_template(matrix_str, template):
        for i in range(len(template)):
            for j in range(len(template[i])):
                if template[i][j] == '1' and matrix_str[i][j] != '1':
                    return False
        return True
    
    # Check each template
    for shape, template in templates.items():
        if matches_template(matrix_str, template):
            return shape
    
    return "-1"

def Solution2():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    C = int(data[index])
    index += 1
    results = []
    
    for _ in range(C):
        N = int(data[index])
        index += 1
        binary_array = data[index]
        index += 1
        
        # Create the NxN matrix
        matrix = []
        for i in range(N):
            row = list(map(int, binary_array[i*N:(i+1)*N]))
            matrix.append(row)
        
        # Detect the shape
        shape = detect_shape(matrix, N)
        results.append(shape)
    
    # Print the results
    print(" ".join(results))

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