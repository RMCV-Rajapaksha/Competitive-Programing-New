# Read input values
N, K = map(int, input().split())
elasticities = list(map(int, input().split()))

# Function to calculate number of tiles hit by a ball with elasticity E
def tiles_hit(E, N):
    return set(range(E, N+1, E))

# Initialize a set to store all unique tiles hit by any ball
hit_tiles = set()

# Calculate tiles hit by each ball and update the set
for elasticity in elasticities:
    hit_tiles.update(tiles_hit(elasticity, N))

# Print the total count of unique tiles hit at least once
print(len(hit_tiles))