def get_optimal_cost(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
        
    # Since array is sorted, pair elements from both ends
    max_pair_sum = 0
    left, right = 0, n-1
    
    while left < right:
        max_pair_sum = max(max_pair_sum, arr[left] + arr[right])
        left += 1
        right -= 1
        
    # If odd length, consider the middle element
    if n % 2 == 1:
        max_pair_sum = max(max_pair_sum, arr[n//2])
        
    return max_pair_sum

def solve(N, Q, A, queries):
    result = []
    
    for x in queries:
        total = 0
        
        # For each possible left endpoint
        for left in range(N):
            # For each possible right endpoint
            right = left
            while right < N:
                # Get optimal cost for current subarray
                curr_cost = get_optimal_cost(A[left:right+1])
                
                # If cost exceeds x, no point checking longer subarrays
                if curr_cost > x:
                    break
                    
                # Add to result if optimal cost ≤ x
                total += A[right] - A[left]
                right += 1
                
        result.append(total)
        
    return result

# Read input
def process_input(input_lines):
    N, Q = map(int, input_lines[0].split())
    A = list(map(int, input_lines[1].split()))
    queries = [int(input_lines[i+2]) for i in range(Q)]
    return N, Q, A, queries

# Test with given examples
test_cases = [
    ["10 5",
     "4 4 5 5 10 10 10 10 14 14",
     "4", "24", "9", "5", "12"],
    ["10 4",
     "0 0 0 6 18 18 18 20 20 20",
     "40", "19", "1", "26"]
]

for test in test_cases:
    N, Q, A, queries = process_input(test)
    result = solve(N, Q, A, queries)
    print("\nInput:")
    print("\n".join(test))
    print("\nOutput:")
    for r in result:
        print(r)