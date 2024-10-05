def can_cross(bridge_status, time_needed):
    length = len(bridge_status[0])
    for start in range(length - time_needed + 1):
        if all(all(bridge_status[d][start + t] == '0' for t in range(time_needed)) for d in range(len(bridge_status))):
            return start + time_needed
    return -1

def find_crossing_times(test_cases):
    results = []
    for case in test_cases:
        D, times, bridge_status = case
        end_time = 0
        for time_needed in times:
            end_time = can_cross(bridge_status, time_needed)
            if end_time == -1:
                results.append("H")
                break
        else:
            results.append(str(end_time))
    return results

# Sample Input
C = int(input())
test_cases = []
for _ in range(C):
    D = int(input())
    times = list(map(int, input().split()))
    bridge_status = [input().strip() for _ in range(D)]
    test_cases.append((D, times, bridge_status))

# Get the results
results = find_crossing_times(test_cases)

# Print the results
print(" ".join(results))