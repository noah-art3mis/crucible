import sys


def are_you_sure(total_cost: float, danger_mode: bool) -> None:
    if not danger_mode:
        if not _ask_permission(total_cost):
            sys.exit(0)


def _ask_permission(total_cost: float) -> bool:
    while True:
        print(f"This will cost around ${total_cost:.2f}.")
        response = input("Are you sure you want to continue? (y/n): ").strip().lower()
        
        if response == "y":
            print("Permission granted. Continuing...")
            return True
        elif response == "n":
            print("Permission denied. Exiting...")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
