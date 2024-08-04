import math
import os
import random
import re
import sys

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
import heapq

def getCost(g_nodes, g_from, g_to, g_weight):
    # Initialize adjacency list for the graph
    graph = [[] for _ in range(g_nodes + 1)]
    for u, v, w in zip(g_from, g_to, g_weight):
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Initialize the min-heap and cost array
    min_heap = [(0, 1)]  # (current cost, starting node)
    costs = [float('inf')] * (g_nodes + 1)
    costs[1] = 0
    
    # Dijkstra's algorithm to find the minimum cost path
    while min_heap:
        current_cost, u = heapq.heappop(min_heap)

        for v, w in graph[u]:
            new_cost = max(0, w - current_cost)
            if current_cost + new_cost < costs[v]:
                costs[v] = current_cost + new_cost
                heapq.heappush(min_heap, (costs[v], v))
    
    # Output the result
    result = costs[g_nodes]
    if result == float('inf'):
        print("NO PATH EXISTS")
    else:
        print(result)


if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)