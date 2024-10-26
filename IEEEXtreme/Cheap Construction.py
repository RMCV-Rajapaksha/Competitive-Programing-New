def find_min_string_lengths(S):
    N = len(S)
    result = [0] * N

    # Memoization dictionary for storing connected component counts
    memo_components = {}

    # Union-Find functions
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, x, y):
        rootX = find(parent, x)
        rootY = find(parent, y)
        if rootX != rootY:
            parent[rootX] = rootY

    # Function to count connected components based on a given substring T
    def count_connected_components(T):
        if T in memo_components:
            return memo_components[T]

        parent = list(range(N + 1))
        t_len = len(T)

        # Find all occurrences of T in S and union indices
        i = 0
        while i <= N - t_len:
            if S[i:i + t_len] == T:
                for j in range(i + 1, i + t_len):
                    union(parent, i + 1, j + 1)
            i += 1

        # Count unique roots
        component_count = len(set(find(parent, x) for x in range(1, N + 1)))
        memo_components[T] = component_count
        return component_count

    # Check for each possible number of components
    for k in range(1, N + 1):
        min_length = float('inf')
        found = False

        # Try each possible substring length for minimal length search
        for length in range(1, N + 1):
            for start in range(N - length + 1):
                T = S[start:start + length]
                component_count = count_connected_components(T)
                
                if component_count == k:
                    min_length = min(min_length, length)
                    found = True
                    break  # Found the minimum length for this k, exit early
            
            if found:
                result[k - 1] = min_length
                break

        if not found:
            result[k - 1] = 0

    return result

# Example usage
S = input().strip()
result = find_min_string_lengths(S)
print(" ".join(map(str, result)))
