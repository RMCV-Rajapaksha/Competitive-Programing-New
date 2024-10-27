def solve_stones_game(r1, b1, r2, b2):
    # State: (alice_red, alice_blue, bob_red, bob_blue, alice_turn)
    # Value: probability of Alice winning from this state
    dp = {}
    
    def get_state_value(ar, ab, br, bb, alice_turn):
        # Base cases - someone has lost
        if ar == 0 or ab == 0:
            return 0.0  # Alice lost
        if br == 0 or bb == 0:
            return 1.0  # Bob lost
            
        state = (ar, ab, br, bb, alice_turn)
        if state in dp:
            return dp[state]
            
        if alice_turn:
            # Alice is player A
            # Try both colors and take the maximum probability
            prob_red = 0
            prob_blue = 0
            
            # If Alice chooses red
            # Bob will guess the color that gives him the best chance
            guess_red_value = get_state_value(ar - 1, ab, br, bb, False) * 0.5 + \
                            get_state_value(ar, ab, br - 1, bb, False) * 0.5
            guess_blue_value = get_state_value(ar, ab, br, bb - 1, False)
            prob_red = guess_red_value if guess_red_value <= guess_blue_value else guess_blue_value
            
            # If Alice chooses blue
            guess_red_value = get_state_value(ar - 1, ab, br, bb, False)
            guess_blue_value = get_state_value(ar, ab - 1, br, bb, False) * 0.5 + \
                             get_state_value(ar, ab, br, bb - 1, False) * 0.5
            prob_blue = guess_red_value if guess_red_value <= guess_blue_value else guess_blue_value
            
            dp[state] = max(prob_red, prob_blue)
            
        else:
            # Bob is player A
            # Try both colors and take the minimum probability (worst for Alice)
            prob_red = 1
            prob_blue = 1
            
            # If Bob chooses red
            # Alice will guess the color that gives her the best chance
            guess_red_value = get_state_value(ar - 1, ab, br, bb, True) * 0.5 + \
                            get_state_value(ar, ab, br - 1, bb, True) * 0.5
            guess_blue_value = get_state_value(ar, ab, br, bb - 1, True)
            prob_red = guess_red_value if guess_red_value >= guess_blue_value else guess_blue_value
            
            # If Bob chooses blue
            guess_red_value = get_state_value(ar - 1, ab, br, bb, True)
            guess_blue_value = get_state_value(ar, ab - 1, br, bb, True) * 0.5 + \
                             get_state_value(ar, ab, br, bb - 1, True) * 0.5
            prob_blue = guess_red_value if guess_red_value >= guess_blue_value else guess_blue_value
            
            dp[state] = min(prob_red, prob_blue)
            
        return dp[state]
    
    return get_state_value(r1, b1, r2, b2, True)

def main():
    # Read input
    r1, b1, r2, b2 = map(int, input().split())
    
    
    result = solve_stones_game(r1, b1, r2, b2)
    print(f"{result:.9f}")

if __name__ == "__main__":
    main()