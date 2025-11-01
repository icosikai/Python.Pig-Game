#Project 1: Pig game.
import random

#Create a player class.
class Players():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    #Player's "roll" function.
    def roll(self):
        print(f"\n{self.name}'s turn has started!")
        ask_roll = input(f"\n{self.name}, would you like to roll the die this turn? (Y/N): ").upper()
        while ask_roll == "Y":
            die = random.randint(1, 6)

            if die != 1:
                print(f"{self.name}, You rolled a {die} on the die!")
                self.score += die
                print(f"{die} points have been added to your score. Now you have {self.score} points! \n")
                if self.score >= 50:
                    break
                ask_roll = input("Would you like to roll again? (Y/N): ").upper()

            else:
                print("Oops! you rolled a 1. Your score resets to 0.")
                self.score = 0
                break

        print(f"{self.name}'s turn has ended. They recieved {self.score} points this turn!")

    def display_scores(self):
        print(f"{self.name}'s final score: {self.score}")

player_list = []

num_players = int(input("Enter the number of players (2-4): "))
print("")
max_scores = 50

while num_players < 2 or num_players > 4:
    num_players = int(input("Player number was out of range. Try again. (2-4 players): "))

for i in range(num_players):
    player_names = input(f"Enter the name of player {i + 1}: ")
    player = Players(player_names, 0)
    player_list.append(player)

current_num = 0
current_player = player_list[current_num]

while all(player.score < max_scores for player in player_list):
    current_player.roll()
    if current_player.score >= max_scores:
        break

    current_num = (current_num + 1) % num_players
    current_player = player_list[current_num]

print("\nThe game has ended! Here are the final results:\n")

for players in player_list:
    players.display_scores()


print("\nThe winner of the game is...")

print(f"{current_player.name} with {current_player.score} points!")
