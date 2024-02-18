import random

class Team:
    def __init__(self, name):
        self.name = name
        self.lives = 100  # Make lives an instance variable accessible with self.
        
    def get_random_number(self):  # Method names in Python typically use snake_case.
        return random.randint(1, 6)

team1 = Team('Team 1')
team2 = Team('Team 2')

while team1.lives > 0 and team2.lives > 0:  # Use 'and' to continue while both teams have lives.
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
    elif team2.lives == 0:
        print(f"Team 2 has lost the game! Team 1 had {team1.lives} lives left!")