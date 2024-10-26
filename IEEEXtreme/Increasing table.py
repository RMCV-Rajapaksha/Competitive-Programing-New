def solve(N, A, B):
    MOD = 998244353
    
    # Convert A and B to sets for O(1) lookup
    A = set(A)
    B = set(B)
    
    # dp[pos][cnt1][cnt2] represents number of ways to fill the table
    # up to position pos using cnt1 numbers in first row and cnt2 in second row
    dp = {}
    
    def count_smaller(x, used):
        # Count numbers smaller than x that are not in used
        result = 0
        for i in range(1, x):
            if i not in used:
                result += 1
        return result
    
    def count_between(x, y, used):
        # Count numbers between x and y (exclusive) that are not in used
        result = 0
        for i in range(x + 1, y):
            if i not in used:
                result += 1
        return result
    
    def recurse(pos, last1, last2, used):
        if pos == N:
            return 1
            
        if (pos, last1, last2, tuple(sorted(used))) in dp:
            return dp[(pos, last1, last2, tuple(sorted(used)))]
            
        result = 0
        
        # Get available numbers for first row
        avail1 = []
        for i in range(last1 + 1, 2*N + 1):
            if i not in used and i not in B:
                avail1.append(i)
        
        # For each valid number in first row
        for num1 in avail1:
            # Get available numbers for second row
            avail2 = []
            for i in range(max(last2 + 1, num1 + 1), 2*N + 1):
                if i not in used and i != num1 and i not in A:
                    avail2.append(i)
            
            # For each valid number in second row
            for num2 in avail2:
                new_used = used | {num1, num2}
                result = (result + recurse(pos + 1, num1, num2, new_used)) % MOD
        
        dp[(pos, last1, last2, tuple(sorted(used)))] = result
        return result
    
    return recurse(0, 0, 0, set())

# Read input
N = int(input())
X, *A = map(int, input().split())
Y, *B = map(int, input().split())

# Print result
print(solve(N, A, B))