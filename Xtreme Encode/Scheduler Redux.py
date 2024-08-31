def minimum_time_required(jobs, k):
    def can_assign(max_time):
        workers = 1
        curr_time = 0
        for job in jobs:
            if curr_time + job > max_time:
                workers += 1
                curr_time = 0
            curr_time += job
        return workers <= k

    low, high = max(jobs), sum(jobs)
    while low < high:
        mid = (low + high) // 2
        if can_assign(mid):
            high = mid
        else:
            low = mid + 1
    return low

# Input reading
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_jobs = int(data[0])
    num_workers = int(data[1])
    jobs = list(map(int, data[2:2 + num_jobs]))
    jobs = [2**i for i in jobs]
    
    # Call the function and print the result
    result = minimum_time_required(jobs, num_workers)
    print(result % (10**9 + 7))