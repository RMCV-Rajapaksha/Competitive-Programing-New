def isMatch(s: str, p: str) -> bool:
    # Create a DP table with (len(s) + 1) x (len(p) + 1)
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Empty string matches with empty pattern
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc., where * matches zero occurrences
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # If current characters match or pattern has '.', set dp[i][j] to dp[i-1][j-1]
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # If the pattern has '*', there are two cases:
                # 1. Match zero of the previous character: dp[i][j] = dp[i][j-2]
                # 2. Match one or more of the previous character if it matches s[i-1]
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))
    
    return dp[len(s)][len(p)]

# Get input from the user
if __name__ == "__main__":
    try:
        s = input().strip()
        p = input().strip()
        
        # Check if the string matches the pattern
        result = isMatch(s, p)
        
        # Print "true" or "false" as lowercase strings
        print("true" if result else "false")
    except Exception as e:
        print(f"An error occurred: {e}")