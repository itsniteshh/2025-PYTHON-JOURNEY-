from art import logo, vs
from game_data import data
import random

# Function to select random player
def get_random_player():
    """Gets a random player from the data"""
    return random.choice(data)

# Function to extract player details
def get_player_details(player):
    """Extracts and formats player details"""
    name = player["name"]
    followers = player["follower_count"]
    description = player["description"]
    country = player["country"]
    return name, followers, description, country

# Function to compare followers
def compare_followers(a_followers, b_followers):
    """Returns 'a' if player A has more followers, else 'b'"""
    if a_followers > b_followers:
        return "a"
    else:
        return "b"

# Main game logic
def play_game():
    print(logo)  # Display logo
    score = 0
    game_active = True

    # Get initial players
    player_a = get_random_player()
    player_b = get_random_player()

    # Ensure both players are different
    while player_b == player_a:
        player_b = get_random_player()

    while game_active:
        # Get player details for display
        a_name, a_followers, a_description, a_country = get_player_details(player_a)
        b_name, b_followers, b_description, b_country = get_player_details(player_b)

        # Show the comparison
        print(f"Compare A: {a_name}, a {a_description}, from {a_country}")
        print(vs)
        print(f"Compare B: {b_name}, a {b_description}, from {b_country}")

        # Get user input
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Determine the correct answer
        correct_answer = compare_followers(a_followers, b_followers)

        if guess == correct_answer:
            # Correct answer
            score += 1
            print(f"You're right! Current score: {score}")

            # Update players
            if correct_answer == "a":
                # Player B gets replaced
                player_b = get_random_player()
                while player_b == player_a:  # Ensure no duplicates
                    player_b = get_random_player()
            else:
                # Player A becomes Player B, and new Player A is chosen
                player_a = player_b
                player_b = get_random_player()
                while player_b == player_a:
                    player_b = get_random_player()
        else:
            # Wrong answer
            print(f"Sorry, that's incorrect. Final score: {score}")
            game_active = False

# Start the game
play_game()
