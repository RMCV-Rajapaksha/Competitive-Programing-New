from collections import defaultdict
import sys

def main():
    # Fast I/O
    input = sys.stdin.readline
    
    MOD = 10**9 + 7
    
    # Read input
    N = int(input())
    weights = list(map(int, input().split()))
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(N-1):
        u, v = map(lambda x: int(x)-1, input().split())  # Convert to 0-based indexing
        adj[u].append(v)
        adj[v].append(u)
    
    # Build parent and depth arrays using DFS
    parent = [-1] * N
    depth = [0] * N
    
    def dfs(v, p, d):
        parent[v] = p
        depth[v] = d
        for u in adj[v]:
            if u != p:
                dfs(u, v, d + 1)
    
    dfs(0, -1, 0)
    
    # Find LCA (Lowest Common Ancestor) of two nodes
    def lca(u, v):
        while depth[u] > depth[v]:
            u = parent[u]
        while depth[v] > depth[u]:
            v = parent[v]
        while u != v:
            u = parent[u]
            v = parent[v]
        return u
    
    # Get nodes on path between two vertices
    def get_path_nodes(u, v):
        common = lca(u, v)
        path = set()
        
        # Add nodes from u to LCA
        curr = u
        while curr != common:
            path.add(curr)
            curr = parent[curr]
            
        # Add nodes from v to LCA
        curr = v
        while curr != common:
            path.add(curr)
            curr = parent[curr]
            
        path.add(common)
        return path
    
    # Get Steiner tree nodes for a set of terminals
    def get_steiner_nodes(terminals):
        if len(terminals) <= 1:
            return terminals
        
        nodes = set()
        terminals = list(terminals)
        
        # For each pair of terminals, add all nodes on their path
        for i in range(len(terminals)):
            for j in range(i+1, len(terminals)):
                nodes.update(get_path_nodes(terminals[i], terminals[j]))
        
        return nodes
    
    # For each size k
    result = [0] * N
    curr_subset = []
    
    def process_subset(size):
        nodes = get_steiner_nodes(set(curr_subset))
        total = sum(weights[node] for node in nodes)
        result[size-1] = (result[size-1] + total) % MOD
    
    # Generate all subsets of each size using backtracking
    def generate_subsets(pos, size, target_size):
        if len(curr_subset) == target_size:
            process_subset(target_size)
            return
        
        for i in range(pos, N):
            curr_subset.append(i)
            generate_subsets(i+1, size+1, target_size)
            curr_subset.pop()
    
    # Process all subset sizes
    for k in range(1, N+1):
        generate_subsets(0, 0, k)
    
    # Print results
    for r in result:
        print(r)

if __name__ == "__main__":
    main()