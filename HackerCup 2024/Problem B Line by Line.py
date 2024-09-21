def solve():
    T = int(input())  # Number of test cases
    for t in range(1, T + 1):
        # Read N and P from input
        N, P = map(int, input().split())
        
        # Convert P from percentage to probability
        P = P / 100
        
        # Compute P_new = P ^ ((N-1)/N)
        P_new = P ** ((N - 1) / N)
        
        # Convert P_new back to percentage
        P_new *= 100
        
        # Calculate the required increase in probability
        increase = P_new - (P * 100)
        
        # Output the result
        print(f"Case #{t}: {increase:.12f}")

# Example usage:
solve()
