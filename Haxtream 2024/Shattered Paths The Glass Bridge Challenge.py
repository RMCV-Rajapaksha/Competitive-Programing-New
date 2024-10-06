def solve_squid_game():
    # Reading the number of test cases
    C = int(input().strip())

    # Processing each test case
    for _ in range(C):
        binary_input = input().strip()

        # First 6 bits for number of steps (S)
        S = int(binary_input[:6], 2)

        # Next 6 bits for number of tiles (N)
        N = int(binary_input[6:12], 2)

        # Remaining part is the tempered glass map
        tempered_map = binary_input[12:]
        
        # Check the tempered tiles for each step
        path = []
        for i in range(S):
            # Extract the part corresponding to the ith step
            step_tiles = tempered_map[i * N:(i + 1) * N]
            
            # Find which lane has tempered glass
            tempered_lane = None
            for lane, tile in enumerate(step_tiles):
                if tile == '1':  # Tempered glass found
                    tempered_lane = lane + 1
                    break
            
            if tempered_lane:
                path.append(tempered_lane)
            else:
                path = ["DEAD"]
                break
        
        print(" ".join(map(str, path)))

# Test the function
solve_squid_game()
