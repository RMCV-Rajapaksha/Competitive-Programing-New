def can_travelers_cross(N, K, speeds):
    # Sort speeds in ascending order
    speeds.sort()
    
    # If there's only one traveler, check if their time is within K
    if N == 1:
        return speeds[0] <= K
    
    total_time = 0
    left = N - 1  # Start from the last (slowest) traveler

    while left >= 3:
        # Two possible strategies:
        # 1. Send the two fastest first, then the fastest returns
        # 2. Send the two slowest first, then the second fastest returns
        
        # Option 1: fastest+second fastest cross, fastest returns
        option1 = 2 * speeds[1] + speeds[0] + speeds[left]
        # Option 2: slowest+second slowest cross, fastest returns
        option2 = 2 * speeds[0] + speeds[left] + speeds[left-1]
        
        total_time += min(option1, option2)
        left -= 2  # Two people have crossed
    
    # Now handle the base cases when 3 or fewer people are left
    if left == 2:
        total_time += speeds[2] + speeds[0] + speeds[1]  # 3 people left
    elif left == 1:
        total_time += speeds[1]  # 2 people left
    else:
        total_time += speeds[0]  # 1 person left

    return total_time <= K

def solve():
    T = int(input())  # Number of test cases
    for t in range(1, T+1):
        N, K = map(int, input().split())
        speeds = [int(input()) for _ in range(N)]
        
        if can_travelers_cross(N, K, speeds):
            print(f"Case #{t}: YES")
        else:
            print(f"Case #{t}: NO")

# Example usage:
solve()
