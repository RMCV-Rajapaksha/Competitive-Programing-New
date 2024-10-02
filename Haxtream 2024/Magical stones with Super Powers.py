def count_powerful_stones(states):
    freq = {}
    for state in states:
        freq[state] = freq.get(state, 0) + 1
    powerful_stones = 0
    for count in freq.values():
        if count > 1:
            powerful_stones += 1
    return powerful_stones

def get_next_states(states):
    return [state for state in states]

def try_combinations(states, spells_left, target_stones, memo=None):
    if memo is None:
        memo = {}
    
    state_key = (tuple(sorted(states)), spells_left)
    if state_key in memo:
        return memo[state_key]
    
    current_powerful = count_powerful_stones(states)
    
    if current_powerful == target_stones:
        return True
    
    if spells_left == 0:
        return False
    
    next_states = get_next_states(states)
    result = try_combinations(next_states, spells_left - 1, target_stones, memo)
    
    memo[state_key] = result
    return result

def min_spells_for_k_stones(N, initial_states, K):
    if count_powerful_stones(initial_states) == K:
        return 0
    
    for spells in range(1, N + 1):
        if try_combinations(initial_states, spells, K):
            return spells
    
    return -1

def solve_magical_stones():
    N = int(input())
    initial_states = list(map(int, input().split()))
    Q = int(input())
    
    results = []
    for _ in range(Q):
        K = int(input())
        result = min_spells_for_k_stones(N, initial_states, K)
        results.append(str(result))
    
    print(" ".join(results))

solve_magical_stones()
