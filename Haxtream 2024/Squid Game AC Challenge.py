def solve_ac_challenge(s):
    N = len(s)
    # Convert string to list of integers
    ACs = [int(c) for c in s]
    
    # dp[mask] represents minimum switches needed to reach state 'mask'
    dp = [float('inf')] * (1 << N)
    # Initial state
    initial_mask = 0
    for i in range(N):
        if ACs[i] == 1:
            initial_mask |= (1 << i)
    
    # Base case - initial state needs 0 switches
    dp[initial_mask] = 0
    
    # Process all possible states
    queue = [initial_mask]
    while queue:
        curr_mask = queue.pop(0)
        curr_switches = dp[curr_mask]
        
        # Try switching each AC
        for i in range(N):
            # Check if we can switch AC i according to rules
            if i == N-1 or ((curr_mask & (1 << (i+1))) and 
                           not (curr_mask & ((1 << (N-i-2)) - 1) << (i+2))):
                # Switch AC i
                next_mask = curr_mask ^ (1 << i)
                # If we found a better way to reach next_mask
                if dp[next_mask] > curr_switches + 1:
                    dp[next_mask] = curr_switches + 1
                    queue.append(next_mask)
    
    # Return minimum switches needed to reach all-off state (0)
    return dp[0] if dp[0] != float('inf') else -1

# Read input
s = input().strip()
result = solve_ac_challenge(s)
print(result)