def minimum_comparisons(n, weights):

    if n == 1:
        return 0
    
    comparisons = 0
 
    weights.sort()

    while len(set(weights)) > 1:
        comparisons += 1
        mid = len(weights) // 2
        left_half = weights[:mid]
        right_half = weights[mid:]
        
     
        if sum(left_half) > sum(right_half):
            weights = left_half
        else:
            weights = right_half
    
    return comparisons

if __name__ == "__main__":
    n = int(input())  # Number of balls
    weights = list(map(int, input().split()))  # List of weights
    print(minimum_comparisons(n, weights))
