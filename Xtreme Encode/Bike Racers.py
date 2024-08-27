def can_match_within_time(distances, M, N, K, max_dist_squared):
    from collections import defaultdict
    
    def dfs(biker, visited):
        for bike in adj_list[biker]:
            if visited[bike]:
                continue
            visited[bike] = True
            if bike_match[bike] == -1 or dfs(bike_match[bike], visited):
                bike_match[bike] = biker
                return True
        return False

    adj_list = defaultdict(list)
    for i in range(M):
        for j in range(N):
            if distances[i][j] <= max_dist_squared:
                adj_list[i].append(j)

    bike_match = [-1] * N
    matched = 0

    for biker in range(M):
        visited = [False] * N
        if dfs(biker, visited):
            matched += 1
        if matched >= K:
            return True
    
    return False

def min_time_squared(M, N, K, bikers, bikes):
    distances = [[(bikes[j][0] - bikers[i][0]) ** 2 + (bikes[j][1] - bikers[i][1]) ** 2 for j in range(N)] for i in range(M)]
    
    lo, hi = 0, max(max(row) for row in distances)
    
    while lo < hi:
        mid = (lo + hi) // 2
        if can_match_within_time(distances, M, N, K, mid):
            hi = mid
        else:
            lo = mid + 1
            
    return lo

# Reading input from console
if __name__ == "__main__":
    M, N, K = map(int, input().split())
    bikers = [tuple(map(int, input().split())) for _ in range(M)]
    bikes = [tuple(map(int, input().split())) for _ in range(N)]
    
    result = min_time_squared(M, N, K, bikers, bikes)
    print(result)
