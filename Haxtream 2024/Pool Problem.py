def longest_suffix_in_subsequence(s, queries):
    results = []
    
    for p in queries:
        i = len(p) - 1  
        j = len(s) - 1  
        
      
        matched_length = 0
        while i >= 0 and j >= 0:
            if p[i] == s[j]:
                matched_length += 1
                i -= 1  
            j -= 1  
        
        results.append(matched_length)
    
    return results


# Input
s = input().strip()
q = int(input().strip())
queries = [input().strip() for _ in range(q)]

# Output
result = longest_suffix_in_subsequence(s, queries)
for res in result:
    print(res)