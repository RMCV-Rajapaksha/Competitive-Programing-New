import itertools

def calculate_min_swaps_to_target(perm, target):
    """
    Calculate the minimum adjacent swaps needed to transform `perm` into `target`.
    Uses inversion count by mapping permutation to target indices.
    """
    perm_indices = {value: i for i, value in enumerate(perm)}
    target_indices = [perm_indices[value] for value in target]
    
    # Count inversions in target_indices which gives minimum adjacent swaps needed
    inv_count = 0
    for i in range(len(target_indices)):
        for j in range(i + 1, len(target_indices)):
            if target_indices[i] > target_indices[j]:
                inv_count += 1
    return inv_count

def target_pattern(n):
    """
    Generate the target pattern for a given n.
    """
    half = (n + 1) // 2
    ascending_part = list(range(1, half + 1))
    descending_part = list(range(n, half, -1))
    return ascending_part + descending_part

def sum_min_swaps_all_permutations(n, m):
    target = target_pattern(n)
    all_perms = itertools.permutations(range(1, n + 1))
    total_min_swaps = 0
    
    for perm in all_perms:
        min_swaps = calculate_min_swaps_to_target(perm, target)
        total_min_swaps = (total_min_swaps + min_swaps) % m

    return total_min_swaps

# Input example
N, M = 3, 107
print(sum_min_swaps_all_permutations(N, M))