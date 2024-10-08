def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        number = data[idx]
        idx += 1
        
        valid_materials = set(str(i) for i in range(1, N + 1))
        
        dp = [0] * (len(number) + 1)
        dp[0] = 1  # There is one way to split an empty string
        
        for i in range(1, len(number) + 1):
            for l in range(1, len(str(N)) + 1):
                if i >= l:
                    substr = number[i - l:i]
                    if substr in valid_materials:
                        dp[i] += dp[i - l]
        
        result = dp[len(number)]
        results.append(str(result) if result > 0 else "-1")
    
    print("\n".join(results))

solve()