import random
import time
class Team:
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
        self.battles_won = 0
        
    def get_random_number(self):
        return random.randint(1, 6)
    
teams_lives = int(input("How many lived would you both teams to have?"))
team1 = Team('Team 1', teams_lives)
team2 = Team('Team 2', teams_lives)

def reset_lives(team1, team2):
    team1.lives = teams_lives
    team2.lives = teams_lives

while team1.battles_won < 5 and team2.battles_won < 5:
    reset_lives(team1, team2)
    
    while team1.lives > 0 and team2.lives > 0:
        
        team1roll = team1.get_random_number()
        team2roll = team2.get_random_number()
        print(f"Team 1's roll is {team1roll}, Team 2's roll is {team2roll}.")
        if team1roll > team2roll:
            team2.lives -= 1
            print(f"Team 1 wins! Team 2 has {team2.lives} lives left!")
        elif team1roll < team2roll:
            team1.lives -= 1
            print(f"Team 2 wins! Team 1 has {team1.lives} lives left!")
        else:
            print("It's a tie! Neither team loses a life!")
            
        if team1.lives == 0:
            print(f"Team 1 has lost the game! Team 2 had {team2.lives} lives left!")
            team2.battles_won += 1
            print(f"Team 2 has won this battle and is at {team2.battles_won} battles won!")
            break
        
        elif team2.lives == 0:
            print(f"Team 2 has lost the game! Team 1 had {team1.lives} lives left!")
            team1.battles_won += 1
            print(f"Team 1 has won this battle and is at {team1.battles_won} battles won!")
            break
        time.sleep(5)
    if team1.battles_won == 5:
        print(f"Team 1 has won the 5 battle war! Team 2 was a {team2.battles_won} victories.")
        
    elif team2.battles_won == 5:
        print(f"Team 2 has won the 5 battle war! Team 1 was at {team1.battles_won} victories.")
    
    else:
        print("On to the next battle!")
