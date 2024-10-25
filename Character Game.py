import random

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.position = "Start"

        self.spawn()
        
    def spawn(self):
        print(f"{self.name} are welcome")

    def move(self, direction):
        print(f"{self.name} move {direction}")

hero = Character("You", 100)

hero.move("left and right, please go ahead and experience what the forest has to offer!")

def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are paths to the left and right.")
    choice = input("Do you want to go left or right? (left/right): ").lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        start_game()

def left_path():
    print("You just walked down the left path and encountered a wild animal!")
    choice = input("Do you want to run or fight? (run/fight): ").lower()

    if choice == "run":
        print("Right choice mate! You ran away safely and survived!")
    elif choice == "fight":
        print("My Guy! You fought bravely but the wild beast overpowers you. Game over!")
    else:
        print("Invalid choice. Please type 'run' or 'fight'.")
        left_path()
            

def right_path():
        print("You just walked down the right path and found a treasure chest!")
        choice = input("Do you want to open it? (yes/no): ").lower()

        if choice == "yes":
            print("You just opened the chest and found gold, jewels and cash. You win!")
        elif choice == "no":
            print("You decided to leave the chest and walked away. You managed to survive!")
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")
            

start_game()