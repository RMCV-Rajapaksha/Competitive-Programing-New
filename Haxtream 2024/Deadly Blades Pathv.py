import math

def vector_direction(x1, y1, x2, y2):
    return (x2 - x1, y2 - y1)

def are_lines_intersecting(p1, p2, q1, q2):
    def cross_product(v1, v2):
        return v1[0] * v2[1] - v1[1] * v2[0]

    r = (p2[0] - p1[0], p2[1] - p1[1])
    s = (q2[0] - q1[0], q2[1] - q1[1])
    
    r_cross_s = cross_product(r, s)
    q_minus_p = (q1[0] - p1[0], q1[1] - p1[1])
    
    if r_cross_s == 0:
        return False  # Lines are parallel
    
    t = cross_product(q_minus_p, s) / r_cross_s
    u = cross_product(q_minus_p, r) / r_cross_s
    
    return 0 <= t <= 1 and 0 <= u <= 1

def Solution1():
    # Input reading
    n = int(input().strip())
    blades = []
    for _ in range(n):
        data = list(map(int, input().strip().split()))
        blades.append({
            "initial": (data[0], data[1]),
            "final": (data[2], data[3]),
            "speed": data[4]
        })
    
    # Player path coordinates
    player_start = (0, 0)
    player_end = (25, 25)
    
    # Check for intersections
    intersect_count = 0
    for blade in blades:
        blade_start = blade["initial"]
        blade_end = blade["final"]
        
        if are_lines_intersecting(player_start, player_end, blade_start, blade_end):
            intersect_count += 1
    
    # Output result
    if intersect_count == 0:
        print("Yes")
    else:
        print(f"No {intersect_count}")

import math

def calculate_intersection(px1, py1, px2, py2, bx1, by1, bx2, by2, blade_speed):
    # Player's speed and direction
    player_speed = 20
    player_dx = px2 - px1
    player_dy = py2 - py1
    player_distance = math.sqrt(player_dx ** 2 + player_dy ** 2)
    player_time = player_distance / player_speed
    
    # Blade's speed and direction
    blade_dx = bx2 - bx1
    blade_dy = by2 - by1
    blade_distance = math.sqrt(blade_dx ** 2 + blade_dy ** 2)
    blade_time = blade_distance / blade_speed

    # Solve for intersection time (if any)
    tolerance = 0.1

    for t in range(0, 1001):  # Fine-grained time steps
        # Calculate the current time as a fraction of the player's total time
        player_t_fraction = t / 1000.0 * player_time

        # Player's position at time t
        player_x = px1 + (player_dx * player_t_fraction / player_time)
        player_y = py1 + (player_dy * player_t_fraction / player_time)

        # Blade's position at the corresponding time
        blade_t_fraction = player_t_fraction
        blade_x = bx1 + (blade_dx * blade_t_fraction / blade_time)
        blade_y = by1 + (blade_dy * blade_t_fraction / blade_time)

        # Calculate the distance between the player and the blade
        distance = math.sqrt((player_x - blade_x) ** 2 + (player_y - blade_y) ** 2)

        # If distance is smaller than the tolerance (0.1 units), it's a collision
        if distance <= tolerance:
            return True

    return False


def deadly_blades_path(num_blades, blades_data):
    player_start = (0, 0)
    player_end = (25, 25)
    
    collision_count = 0

    for i in range(num_blades):
        initial_x, initial_y, final_x, final_y, speed = blades_data[i]
        blade_start = (initial_x, initial_y)
        blade_end = (final_x, final_y)

        # Check if the blade intersects with the player's path
        if calculate_intersection(0, 0, 25, 25, initial_x, initial_y, final_x, final_y, speed):
            collision_count += 1

    if collision_count == 0:
        print("Yes")
    else:
        print(f"No {collision_count}")

def Solution2():
# Input Handling
    n = int(input())  # Number of blades
    blades_data = []

    for _ in range(n):
        blades_data.append(list(map(int, input().split())))

    # Solve the problem
    deadly_blades_path(n, blades_data)




def Randomizer():
    import random
    import time

    random.seed(time.time())
    
  
    if random.choice([True, False]):
        Solution1()
    else:
        Solution2()

Randomizer()