from collections import defaultdict
import bisect

def preprocess_string(s):
    index_map = defaultdict(list)
    for index, char in enumerate(s):
        index_map[char].append(index)
    return index_map

def longest_suffix_length(s, p):
    index_map = preprocess_string(s)
    max_length = 0
    
    # We will check suffixes of p
    for start in range(len(p)):
        current_suffix = p[start:]  # Create suffix
        current_index = -1  # Start searching from before the beginning of s
        valid = True
        
        for char in current_suffix:
            if char not in index_map:
                valid = False
                break
            
            # Find the first index in s that is greater than current_index
            pos_list = index_map[char]
            next_index = bisect.bisect_right(pos_list, current_index)
            
            if next_index == len(pos_list):
                valid = False
                break
            
            # Update current_index to the found position in s
            current_index = pos_list[next_index]
        
        if valid:
            max_length = max(max_length, len(current_suffix))
    
    return max_length

# Read input
s = input().strip()
q = int(input().strip())

results = []
for _ in range(q):
    p = input().strip()
    results.append(longest_suffix_length(s, p))

# Print results
for result in results:
    print(result)
