def solve():
    # Read input
    N, K = map(int, input().split())
    
    # Convert to list of digits
    digits = list(str(N))
    n = len(digits)
    k = K  # remaining swaps
    
    # For each position
    for i in range(n):
        if k == 0:  # if no more swaps left
            break
            
        # Find maximum digit and its position
        max_val = digits[i]
        max_pos = i
        
        # Look ahead for larger digits we can use
        for j in range(i + 1, n):
            # Skip if this would create leading zero
            if i == 0 and digits[j] == '0':
                continue
            
            # Update max if we find larger digit
            if digits[j] > max_val:
                max_val = digits[j]
                max_pos = j
        
        # If we found a better digit, do the swap
        if max_pos != i:
            digits[i], digits[max_pos] = digits[max_pos], digits[i]
            k -= 1
    
    # Return result as string (avoid any potential integer overflow)
    print(''.join(digits))

# Run solution
solve()