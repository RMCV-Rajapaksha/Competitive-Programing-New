def max_phrases(K, J):
    # Calculate the maximum number of phrases that can be formed
    return min((K + J) // 3, K, J)

# Get input from the console
K, J = map(int, input().split())

# Calculate and print the output
print(max_phrases(K, J))
