from collections import deque

# Function to perform BFS and return distances from a given node
def bfs(start, n, adjacency_list):
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in adjacency_list[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist

def find_equidistant_rooms(n, edges, queries):
    # Build the adjacency list (tree structure)
    adjacency_list = [[] for _ in range(n + 1)]
    for a, b in edges:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    
    results = []
    for x, y in queries:
        # Calculate distances from both x and y to all other nodes
        dist_from_x = bfs(x, n, adjacency_list)
        dist_from_y = bfs(y, n, adjacency_list)
        
        # Count the number of rooms equidistant from both x and y
        count = 0
        for i in range(1, n + 1):
            if dist_from_x[i] == dist_from_y[i]:
                count += 1
        
        results.append(count)
    
    return results

# Read input
n = int(input())  # Number of rooms
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
m = int(input())  # Number of days
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Process the queries and find the number of equidistant rooms
output = find_equidistant_rooms(n, edges, queries)

# Print the results
for result in output:
    print(result)