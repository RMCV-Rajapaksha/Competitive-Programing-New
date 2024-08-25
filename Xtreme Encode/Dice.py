def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def solve(n, k):
    MOD = 998244353
    dp = [0] * (n + 1)
    dp[0] = 1
    for _ in range(1, k + 1):
        ndp = [0] * (n + 1)
        for i in range(1, 7):
            for j in range(i, n + 1):
                ndp[j] = (ndp[j] + dp[j - i]) % MOD
        dp = ndp
    return dp[n] * mod_inverse(k, MOD)

n, k = map(int, input().split())
print(solve(n, k))