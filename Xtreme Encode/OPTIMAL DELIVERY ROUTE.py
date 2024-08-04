def optimal_delivery_route(grid, addresses, max_distance):
 
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    current_position = (0, 0)
    route = [current_position]

    while addresses:
       
        closest_address = None
        closest_distance = float('inf')
        for address in addresses:
            distance = abs(address[0] - current_position[0]) + abs(address[1] - current_position[1])
            if distance < closest_distance:
                closest_address = address
                closest_distance = distance

        if closest_distance > max_distance:
            return []

       
        path = find_path(grid, current_position, closest_address, movements)
        if path is None:
            return []
        route.extend(path[1:])
        current_position = closest_address
        addresses.remove(closest_address)

    
    path = find_path(grid, current_position, (0, 0), movements)
    if path is None:
        return []
    route.extend(path[1:])

    return route


def find_path(grid, start, end, movements):

    queue = [(start, [start])]
    visited = set()
    visited.add(start)
    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == end:
            return path
        for dx, dy in movements:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid)) and (0 <= ny < len(grid[0])) and (grid[nx][ny] == 0) and ((nx, ny) not in visited):
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None



import sys
input = sys.stdin.read
data = input().split()

rows = int(data[0])
cols = int(data[1])
grid = []
index = 2
for _ in range(rows):
    grid.append([int(data[index + i]) for i in range(cols)])
    index += cols

num_addresses = int(data[index])
index += 1
addresses = []
for _ in range(num_addresses):
    x = int(data[index])
    y = int(data[index + 1])
    addresses.append((x, y))
    index += 2

max_distance = int(data[index])


route = optimal_delivery_route(grid, addresses, max_distance)
for point in route:
        print(f"{point[0]} {point[1]}")
        
        
        
        
        
        
        
        
        
        
        
        
# from collections import deque
# import sys

# def optimal_delivery_route(grid, addresses, max_distance):
#     movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     current_position = (0, 0)
#     route = [current_position]
#     total_distance = 0

#     while addresses:
#         closest_address, path_to_address = find_nearest_address(grid, current_position, addresses, movements)
#         if closest_address is None:
#             return []

#         # Calculate the distance and check against max_distance
#         if total_distance + len(path_to_address) - 1 > max_distance:
#             return []

#         # Extend the route with the path to the nearest address
#         route.extend(path_to_address[1:])
#         total_distance += len(path_to_address) - 1
#         current_position = closest_address
#         addresses.remove(closest_address)

#     # Return to the starting point (0,0)
#     return_route = find_path(grid, current_position, (0, 0), movements)
#     if return_route is None or total_distance + len(return_route) - 1 > max_distance:
#         return []

#     total_distance += len(return_route) - 1
#     route.extend(return_route[1:])
    
#     return route

# def find_nearest_address(grid, start, addresses, movements):
#     closest_address = None
#     closest_path = None
#     shortest_distance = float('inf')

#     for address in addresses:
#         path = find_path(grid, start, address, movements)
#         if path is not None and len(path) < shortest_distance:
#             closest_address = address
#             closest_path = path
#             shortest_distance = len(path)

#     return closest_address, closest_path

# def find_path(grid, start, end, movements):
#     rows, cols = len(grid), len(grid[0])
#     queue = deque([(start, [start])])
#     visited = set()
#     visited.add(start)

#     while queue:
#         current, path = queue.popleft()

#         if current == end:
#             return path

#         for dx, dy in movements:
#             nx, ny = current[0] + dx, current[1] + dy

#             if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
#                 queue.append(((nx, ny), path + [(nx, ny)]))
#                 visited.add((nx, ny))

#     return None

# input = sys.stdin.read
# data = input().split()

# rows = int(data[0])
# cols = int(data[1])
# grid = []
# index = 2
# for _ in range(rows):
#     grid.append([int(data[index + i]) for i in range(cols)])
#     index += cols

# num_addresses = int(data[index])
# index += 1
# addresses = []
# for _ in range(num_addresses):
#     x = int(data[index])
#     y = int(data[index + 1])
#     addresses.append((x, y))
#     index += 2

# max_distance = int(data[index])

# route = optimal_delivery_route(grid, addresses, max_distance)
# for point in route:
#     print(f"{point[0]} {point[1]}")