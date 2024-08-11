import math

W, H, A, B, M, C = map(int, input().split())


tiles_horizontal = math.ceil(W / A)
tiles_vertical = math.ceil(H / B)


total_tiles = tiles_horizontal * tiles_vertical


piles_needed = math.ceil(total_tiles / 10)

tiles_cost = piles_needed * M


cut_right = H if W % A != 0 else 0
cut_bottom = W if H % B != 0 else 0
cut_cost = (cut_right + cut_bottom) * C


total_cost = tiles_cost + cut_cost


print(total_cost)
