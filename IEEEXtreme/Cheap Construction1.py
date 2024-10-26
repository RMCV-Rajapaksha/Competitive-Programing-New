def solve(S):
    N = len(S)
    # For each possible string length
    min_length_for_components = [float('inf')] * (N + 1)
    min_length_for_components[N] = 1  # Single letter string gives N components
    
    # Try all possible substring lengths
    for length in range(1, N+1):
        # For each possible starting position
        for start in range(N - length + 1):
            # Get the substring
            T = S[start:start+length]
            components = find_components(S, T, N)
            # Update minimum length needed for this number of components
            min_length_for_components[components] = min(
                min_length_for_components[components], 
                length
            )
    
    # Replace infinities with 0 (impossible cases)
    result = [x if x != float('inf') else 0 for x in min_length_for_components[1:]]
    return result

def find_components(S, T, N):
    # Build adjacency list
    adj = [[] for _ in range(N)]
    
    # For each position in S
    for start in range(N - len(T) + 1):
        if S[start:start+len(T)] == T:
            # Add edges for consecutive positions
            for i in range(start, start + len(T) - 1):
                adj[i].append(i + 1)
                adj[i + 1].append(i)
    
    # Count components using DFS
    visited = [False] * N
    components = 0
    
    def dfs(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                dfs(u)
    
    for v in range(N):
        if not visited[v]:
            components += 1
            dfs(v)
    
    return components


test=input()
result = solve(test)
print(*result)