def solve_tug_of_war(strengths, team_a_size, team_a_indices):
    
    team_a_strength = sum(strengths[i-1] for i in team_a_indices)
    
   
    total_strength = sum(strengths)
    team_b_strength = total_strength - team_a_strength
    

    if team_a_strength > team_b_strength:
        return "Team A wins"
    elif team_b_strength > team_a_strength:
        return "Team B wins"
    else:
        return "Draw"

strengths = list(map(int, input().split()))
team_a_size = int(input())
team_a_indices = list(map(int, input().split()))

result = solve_tug_of_war(strengths, team_a_size, team_a_indices)
print(result)