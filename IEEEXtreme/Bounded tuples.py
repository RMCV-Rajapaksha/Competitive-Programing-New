def solve():
    N, M = map(int, input().split())
    MOD = 998244353
    
    # If no constraints, infinite solutions
    if M == 0:
        return "infinity"
        
    # Read and store constraints
    constraints = []
    variables_in_constraints = set()
    
    for _ in range(M):
        line = list(map(int, input().split()))
        low, high, K = line[0], line[1], line[2]
        indices = [x-1 for x in line[3:3+K]]  # Convert to 0-based indexing
        constraints.append((low, high, indices))
        variables_in_constraints.update(indices)
    
    # Check for infinite case: if any variable is unconstrained
    if len(variables_in_constraints) < N:
        return "infinity"
    
    # Find maximum bound needed to check
    max_val = 0
    for low, high, _ in constraints:
        max_val = max(max_val, high)
    # Limit max_val to a reasonable number since we only need to check
    # enough values to determine if constraints can be satisfied
    max_val = min(max_val, 10**5)
    
    values = [0] * N
    result = 0
    
    def check_constraints():
        """Check if current assignment satisfies all constraints"""
        for low, high, indices in constraints:
            sum_vals = sum(values[i] for i in indices)
            if sum_vals < low or sum_vals > high:
                return False
        return True
        
    def can_extend(pos):
        """Check if partial assignment can be extended to valid solution"""
        for low, high, indices in constraints:
            # Only check constraints where all variables are assigned
            if all(i <= pos for i in indices):
                sum_vals = sum(values[i] for i in indices)
                if sum_vals < low or sum_vals > high:
                    return False
        return True
    
    def dfs(pos):
        nonlocal result
        
        # Base case: all variables assigned
        if pos == N:
            result = (result + 1) % MOD
            return
            
        # Try each value for current position
        for val in range(max_val + 1):
            values[pos] = val
            # Only continue if current partial assignment is valid
            if can_extend(pos):
                dfs(pos + 1)
    
    # Start the search
    dfs(0)
    return result

def main():
    try:
        print(solve())
    except:
        print(0)

if __name__ == "__main__":
    main()