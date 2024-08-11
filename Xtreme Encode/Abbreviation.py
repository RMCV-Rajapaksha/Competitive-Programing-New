def abbreviation(a, b):
    # Initialize the DP table
    n, m = len(a), len(b)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Base case: an empty b can always match an empty a
    dp[0][0] = True
    
    # Fill the DP table
    for i in range(1, n + 1):
        dp[i][0] = dp[i-1][0] and a[i-1].islower()  # We can delete all lowercase letters in a
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1].upper() == b[j-1]:  # Characters match or can be capitalized to match
                dp[i][j] = dp[i-1][j-1] or (dp[i-1][j] and a[i-1].islower())
            else:
                dp[i][j] = dp[i-1][j] and a[i-1].islower()  # We can delete the lowercase letter
    
    return "YES" if dp[n][m] else "NO"

# Input and output
q = int(input().strip())
for _ in range(q):
    a = input().strip()
    b = input().strip()
    print(abbreviation(a, b))