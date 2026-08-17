import numpy as np  # standard way to import numpy conventions
 
def play_guessing_game():
    secret_number = np.random.randint(1, 101)  # 1 to 100 inclusive
    
    # FIX 1: Added commas between list items
    players = ['Player 1', 'Player 2', 'Player 3']
    
    # FIX 2: Standardized variable name to 'closest_diff'
    closest_diff = {player: float('inf') for player in players}
    
    print("===== Welcome to the Guessing Game Tournament =====")
    print("I have a secret number in mind. Each player gets 3 chances to guess the secret number and take the present home 🎁.\n")

    for player in players:
        print(f"--- It's {player}'s turn! ---")

        for attempt in range(1, 4):
            while True:
                try:
                    guess = int(input(f"Attempt {attempt} - Enter your guess: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a whole number.")
            
            difference = abs(secret_number - guess)
            
            if difference < closest_diff[player]:
                closest_diff[player] = difference
            
            if difference == 0: 
                print(f"Spot on! You are a guess pro 👍👍 {player} guessed the exact number!")
                break
            else:
                if guess < secret_number:
                    print("Too low!. Try again")
                else:
                    print("Too high!. Try again")


    print("\n=== Game over! Here are your results ===")
    
    best_overall_difference = min(closest_diff.values())
    winners = [p for p, diff in closest_diff.items() if diff == best_overall_difference]

    print(f"The correct number was: {secret_number}\n")

    if len(winners) > 1:
        print(f"It's a tie between: {', '.join(winners)}! You were all off by {best_overall_difference}.")
    else:
        print(f"🏆 The winner is {winners[0]}! You were only {best_overall_difference} away from the secret number.")

if __name__ == "__main__":
    play_guessing_game()