def calculate_determinant(matrix, n):
    # Base case for 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for i in range(n):
        # Create the submatrix
        submatrix = []
        for j in range(1, n):
            row = []
            for k in range(n):
                if k != i:
                    row.append(matrix[j][k])
            submatrix.append(row)
        
        # Recursively calculate determinant
        sign = (-1) ** i
        det += sign * matrix[0][i] * calculate_determinant(submatrix, n-1)
    
    return det

def count_odd_numbers(row):
    return sum(1 for x in row if x % 2 != 0)

def construct_matrix(n, odd_counts):
    # For n=2, we can try all possible combinations within constraints
    if n == 2:
        possible_numbers = list(range(-5, 6))
        for a in possible_numbers:
            for b in possible_numbers:
                for c in possible_numbers:
                    for d in possible_numbers:
                        matrix = [[a, b], [c, d]]
                        if (calculate_determinant(matrix, 2) == 1 and
                            count_odd_numbers(matrix[0]) == odd_counts[0] and
                            count_odd_numbers(matrix[1]) == odd_counts[1]):
                            return matrix
        return None
    
    # For n≥3, we'll construct an upper triangular matrix with determinant 1
    matrix = [[0] * n for _ in range(n)]
    
    # Set diagonal elements to 1 to ensure determinant is 1
    for i in range(n):
        matrix[i][i] = 1
    
    # Fill remaining elements while maintaining odd number counts
    for i in range(n):
        odd_needed = odd_counts[i]
        odd_current = count_odd_numbers(matrix[i])
        
        # If we need more odd numbers in this row
        while odd_current < odd_needed:
            # Find a position where we can add an odd number
            for j in range(n):
                if j != i and matrix[i][j] == 0:
                    matrix[i][j] = 1
                    odd_current += 1
                    if odd_current == odd_needed:
                        break
        
        # If we need more even numbers in this row
        while odd_current > odd_needed:
            # Find a position where we can add an even number
            for j in range(n):
                if j != i and matrix[i][j] == 1:
                    matrix[i][j] = 2
                    odd_current -= 1
                    if odd_current == odd_needed:
                        break
                        
        # Check if we couldn't satisfy the odd number requirement
        if odd_current != odd_needed:
            return None
    
    # Verify the determinant is 1
    if calculate_determinant(matrix, n) != 1:
        return None
        
    return matrix

def main():
    # Read input
    n = int(input().strip())
    odd_counts = []
    for _ in range(n):
        odd_counts.append(int(input().strip()))
    
    # Try to construct the matrix
    result = construct_matrix(n, odd_counts)
    
    # Output result
    if result is None:
        print(-1)
    else:
        print(1)

if __name__ == "__main__":
    main()