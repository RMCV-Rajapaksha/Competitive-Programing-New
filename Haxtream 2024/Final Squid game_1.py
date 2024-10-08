def can_pass_bridge(players, binary_array):
    time_index = 0  # Start at the first time index
    total_time = len(binary_array[0])  # Length of the binary array
    
    for player_time in players:
        found_interval = False
        
        # Try to find a valid interval for this player
        while time_index <= total_time - player_time:
            all_not_looking = True
            
            # Check if all defenders are not looking during the player's crossing time
            for d in range(len(binary_array)):
                if any(binary_array[d][time_index + t] == '1' for t in range(player_time)):
                    all_not_looking = False
                    break
            
            if all_not_looking:
                found_interval = True
                break
            
            time_index += 1  # Move to the next time index
        
        if not found_interval:
            return 'H'  # Player cannot pass
        
        # Increment the time_index by the time the player takes to cross the bridge
        time_index += player_time
    
    return time_index  # Return the last time index when the last player crosses

# Input Handling
C = int(input())  # number of test cases
results = []
for _ in range(C):
    D = int(input())  # number of defenders
    players = list(map(int, input().split()))  # time consumption of each player
    defenders = []
    for _ in range(D):
        defenders.append(input().strip())  # Read each defender's binary array directly

    binary_array = defenders  # Use the defenders list directly as binary_array
    result = can_pass_bridge(players, binary_array)
    results.append(str(result))  # Collect results

print(' '.join(results))  # Print all results in a single line
