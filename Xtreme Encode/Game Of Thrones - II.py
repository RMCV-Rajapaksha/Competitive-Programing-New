import math

MOD = 10**9 + 7

def solve(s):
    # Step 1: Calculate the frequency of each character
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Step 2: Calculate the factorials up to the length of the string
    n = len(s)
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i-1] * i) % MOD
    
    # Step 3: Count half frequencies and find the central element (odd frequency)
    half_freq_sum = 0
    denominator = 1
    odd_count = 0
    
    for count in freq.values():
        half_freq_sum += count // 2
        denominator = (denominator * fact[count // 2]) % MOD
        if count % 2 != 0:
            odd_count += 1
    
    # Step 4: Calculate the number of palindrome anagrams
    # Use the formula (half_freq_sum)! / (freq[char1]//2)! * (freq[char2]//2)! * ... * (freq[charN]//2)!
    numerator = fact[half_freq_sum]
    result = (numerator * pow(denominator, MOD-2, MOD)) % MOD
    
    # Return the result modulo 10^9 + 7
    return result

# Example usage:
if __name__ == '__main__':
    s = input().strip()
    print(solve(s))
