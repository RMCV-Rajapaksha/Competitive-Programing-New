from collections import deque

def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        for v, capacity in enumerate(graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    
    return max_flow

def solve_voting_problem(n, m, s, p, bus_routes):
    # Initialize the graph with appropriate dimensions
    graph = [[0] * (n + 2) for _ in range(n + 2)]
    
    # Example of how you might populate the graph
    for i in range(n):
        graph[i][n + 1] = float('inf')
    
    # Rest of your function logic
    # ...

    return graph  # or the actual result of your function

# Example usage
n, m, s, p = map(int, input().split())
bus_routes = [list(map(int, input().split())) for _ in range(m)]

result = solve_voting_problem(n, m, s, p, bus_routes)
print(result)