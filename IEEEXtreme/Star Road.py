def solve_with_preprocessing(n, stars, edges):
    
    graph = [[] for _ in range(n)]
    for u, v in edges:
        u, v = u-1, v-1
        graph[u].append(v)
        graph[v].append(u)
    

    degrees = [len(graph[i]) for i in range(n)]
    leaf_nodes = [i for i, deg in enumerate(degrees) if deg == 1]
    
  
    nodes_by_stars = sorted(range(n), key=lambda x: stars[x])
    
    dp = {}
    
    def dfs(node, parent, last_stars):
        state = (node, parent, last_stars)
        if state in dp:
            return dp[state]
        
        current_stars = stars[node]
        max_restaurants = 0
        
        if max_restaurants > n - node:
            return max_restaurants
        
        if current_stars > last_stars:
            current_best = 1
            
            next_nodes = sorted(
                [next_node for next_node in graph[node] if next_node != parent],
                key=lambda x: stars[x],
                reverse=True
            )
            
            for next_node in next_nodes:
                result = dfs(next_node, node, current_stars)
                current_best = max(current_best, 1 + result)
            max_restaurants = max(max_restaurants, current_best)
        
 
        for next_node in graph[node]:
            if next_node != parent:
                result = dfs(next_node, node, last_stars)
                max_restaurants = max(max_restaurants, result)
        
        dp[state] = max_restaurants
        return max_restaurants
    

    max_result = 0
    for leaf in leaf_nodes:
        max_result = max(max_result, dfs(leaf, -1, -1))
    
    return max_result


n = 5
stars = [1, 2, 3, 4, 5]
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]

print(solve_with_preprocessing(n, stars, edges))  