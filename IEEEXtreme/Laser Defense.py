class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

def count_regions_approach1(L, N, M, laser_a_beams, laser_b_beams):
  
    if N == 0 and M == 0:
        return 1

    def on_segment(p, q, r):
        return (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
                q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y))

    def orientation(p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if abs(val) < 1e-10:
            return 0
        return 1 if val > 0 else 2

    def do_intersect(p1, q1, p2, q2):
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and on_segment(p1, p2, q1): return True
        if o2 == 0 and on_segment(p1, q2, q1): return True
        if o3 == 0 and on_segment(p2, p1, q2): return True
        if o4 == 0 and on_segment(p2, q1, q2): return True

        return False

    segments_a = []
    segments_b = []
    
    for direction, coord in laser_a_beams:
        if direction == 'U':
            segments_a.append((Point(0, 0), Point(coord, L)))
        else:
            segments_a.append((Point(0, 0), Point(L, coord)))
    
    for direction, coord in laser_b_beams:
        if direction == 'U':
            segments_b.append((Point(L, 0), Point(coord, L)))
        else:
            segments_b.append((Point(L, 0), Point(0, coord)))

    intersections = 0
    for sa in segments_a:
        for sb in segments_b:
            if do_intersect(sa[0], sa[1], sb[0], sb[1]):
                intersections += 1

    unique_a = len(set(laser_a_beams))
    unique_b = len(set(laser_b_beams))
    return 1 + unique_a + unique_b + intersections

def count_regions_approach2(L, N, M, laser_a_beams, laser_b_beams):
   
    unique_top_cuts = set()
    unique_right_cuts = set()
    unique_left_cuts = set()
    
    for direction, coord in laser_a_beams:
        if direction == 'U':
            unique_top_cuts.add(coord)
        elif direction == 'R':
            unique_right_cuts.add(coord)
    
    for direction, coord in laser_b_beams:
        if direction == 'U':
            unique_top_cuts.add(coord)
        elif direction == 'L':
            unique_left_cuts.add(coord)

    horizontal_cuts = len(unique_top_cuts) + 1
    vertical_cuts = len(unique_right_cuts | unique_left_cuts) + 1

    total_regions = horizontal_cuts * vertical_cuts
    return total_regions

def count_regions(L, N, M, laser_a_beams, laser_b_beams):
  
    if N <= 2 and M <= 2:
        return count_regions_approach2(L, N, M, laser_a_beams, laser_b_beams)
    else:
        return count_regions_approach1(L, N, M, laser_a_beams, laser_b_beams)

# Test cases
def run_tests():
    test_cases = [
        {"name": "Original example", "L": 30, "N": 3, "M": 2, "laser_a": [('U', 10), ('U', 25), ('R', 10)], "laser_b": [('L', 15), ('U', 20)], "expected": 11},
        {"name": "Second example", "L": 20, "N": 3, "M": 3, "laser_a": [('U', 10), ('U', 15), ('R', 10)], "laser_b": [('L', 15), ('U', 5), ('U', 15)], "expected": 14},
        {"name": "No beams", "L": 10, "N": 0, "M": 0, "laser_a": [], "laser_b": [], "expected": 1},
        {"name": "Single beam from each laser", "L": 10, "N": 1, "M": 1, "laser_a": [('U', 5)], "laser_b": [('U', 3)], "expected": 4},
        {"name": "All beams parallel", "L": 10, "N": 2, "M": 2, "laser_a": [('U', 3), ('U', 7)], "laser_b": [('U', 2), ('U', 8)], "expected": 5},
        {"name": "Maximum intersections", "L": 10, "N": 2, "M": 2, "laser_a": [('U', 3), ('R', 3)], "laser_b": [('U', 7), ('L', 7)], "expected": 9}
    ]

    for i, test in enumerate(test_cases, 1):
        result = count_regions(
            test["L"],
            test["N"],
            test["M"],
            test["laser_a"],
            test["laser_b"]
        )
        passed = result == test["expected"]
        print(f"Test {i} ({test['name']}): {'PASSED' if passed else 'FAILED'}")
        if not passed:
            print(f"Expected {test['expected']}, got {result}")
            print(f"Test case: L={test['L']}, N={test['N']}, M={test['M']}")
            print(f"Laser A beams: {test['laser_a']}")
            print(f"Laser B beams: {test['laser_b']}\n")
            

L, N, M = map(int, input().split())


laser_a_beams = []
for _ in range(N):
    direction, coord = input().split()
    laser_a_beams.append((direction, int(coord)))


laser_b_beams = []
for _ in range(M):
    direction, coord = input().split()
    laser_b_beams.append((direction, int(coord)))


result = count_regions(L, N, M, laser_a_beams, laser_b_beams)
print(result)
