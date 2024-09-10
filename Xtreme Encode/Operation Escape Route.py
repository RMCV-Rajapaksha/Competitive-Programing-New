def dfs(node, parent, adj, visited, in_cycle):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            if dfs(neighbor, node, adj, visited, in_cycle):
                in_cycle[node] = True
                return True
        elif neighbor != parent:
            in_cycle[node] = True
            return True
    return False

def find_non_cyclic_cities(n, m, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    visited = [False] * (n + 1)
    in_cycle = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1, adj, visited, in_cycle)
    
    non_cyclic_cities = [i for i in range(1, n + 1) if not in_cycle[i]]
    return sorted(non_cyclic_cities)

# Input reading
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
edges = []
index = 2
for _ in range(m):
    a = int(data[index])
    b = int(data[index + 1])
    edges.append((a, b))
    index += 2

# Output the result
result = find_non_cyclic_cities(n, m, edges)
for city in result:
    print(city)