from collections import defaultdict, deque

def topological_sort(graph, indegree, n):
    # Kahn's Algorithm for Topological Sorting
    topo_order = []
    queue = deque()
    
    # Start with all nodes having zero indegree
    for i in range(1, n + 1):  # Node numbers are 1-based
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return topo_order

def find_max_sum_path(n, weights, edges):
    # Step 1: Build graph and calculate indegrees
    graph = defaultdict(list)
    indegree = [0] * (n + 1)  # Indegree for Kahn's algorithm (1-based index)
    
    for u, v in edges:
        graph[u].append(v)  # Directed edge u -> v
        indegree[v] += 1  # Track incoming edges to node v
    
    # Step 2: Get topological order
    topo_order = topological_sort(graph, indegree, n)
    
    # Step 3: Initialize DP array
    dp = [-float('inf')] * (n + 1)  # Initialize with -infinity for maximum path
    for i in range(1, n + 1):
        dp[i] = weights[i - 1]  # Initialize dp with the weight of the node itself
    
    # Step 4: Dynamic Programming to compute maximum path sums
    for u in topo_order:
        for v in graph[u]:
            dp[v] = max(dp[v], dp[u] + weights[v - 1])
    
    # Step 5: Return the maximum value in dp array
    return max(dp)

# Input handling
n, m = map(int, input().split())  # Number of nodes and edges
weights = list(map(int, input().split()))  # Weights of the nodes
edges = [tuple(map(int, input().split())) for _ in range(m)]  # Edges

# Solve the problem
result = find_max_sum_path(n, weights, edges)
print(result)

