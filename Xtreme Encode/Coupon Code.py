from collections import defaultdict

def count_similar_pairs(codes):
    def generate_variants(code):
        """Generate all variants of the code by replacing each character with a wildcard."""
        variants = []
        for i in range(len(code)):
            if code[i] != '-':
                variant = code[:i] + '?' + code[i+1:]
                variants.append(variant)
        return variants

    # Store the count of each variant
    variant_count = defaultdict(int)
    
    for code in codes:
        variants = generate_variants(code)
        for variant in variants:
            variant_count[variant] += 1
    
    # Calculate the number of similar pairs
    similar_pairs = 0
    for count in variant_count.values():
        if count > 1:
            similar_pairs += count * (count - 1) // 2
    
    return similar_pairs

# Input
n = int(input().strip())
codes = [input().strip() for _ in range(n)]

# Output
result = count_similar_pairs(codes)
print(result)