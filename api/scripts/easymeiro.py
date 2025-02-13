def maze_game(choice: str):
    if choice == "left":
        return "You took the left path and found a treasure!"
    elif choice == "right":
        return "You took the right path and fell into a trap!"
    else:
        return "Invalid choice."

if __name__ == "__main__":
    choice = input("Choose a path: left or right: ").lower()
    print(maze_game(choice))
