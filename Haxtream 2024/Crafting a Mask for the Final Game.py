def count_masks(test_cases):
    results = []
    
    for case in test_cases:
        N, large_number = case
        materials = set(str(i) for i in range(1, N + 1))  # Create a set of valid materials
        
        length = len(large_number)
        dp = [0] * (length + 1)
        dp[0] = 1  # There's one way to make an empty mask
        
        for i in range(1, length + 1):
            for j in range(1, 5):  # Look back up to 4 digits
                if i - j >= 0:
                    part = large_number[i - j:i]
                    if part in materials:
                        dp[i] += dp[i - j]
        
        result = dp[length]
        results.append(result if result > 0 else -1)
    
    return results


# Sample Input
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    large_number = input().strip()
    test_cases.append((N, large_number))

# Get the results
results = count_masks(test_cases)

# Print the results
for res in results:
    print(res)
