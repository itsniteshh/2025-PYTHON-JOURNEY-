from art import logo, vs
from game_data import data
import random
import os

#TODO:1 - randomly choosing A and B for comparison
def compare():
    "getting random details for data"
    
    compare_a = random.choice(data)
    return compare_a

a = compare()
b = compare()

#TODO:2 - Assigning values
def players(compare):
    """assigning details to A and B"""
    
    name = compare["name"]
    follower = compare["follower_count"]
    description = compare["description"]
    country = compare["country"]
    
    return name, follower, description, country

a_name, a_follower, a_description, a_country =players(a)
b_name, b_follower, b_description, b_country = players(b)
    
#TODO:4 - comparing values

def comparing(a_follower, b_follower):
    
    if a_follower >= b_follower:
        return "a"
    else:
        return "b"

#TODO: 3 - MAKING SURE THE GAME RUNS TILL WRONG ASNWER IS PROVIDED
live_game = True
count = 0


while live_game:
    print(logo)
    print(f"Compare A: {a_name}, a {a_description}, from {a_country}")
    print(vs)
    print(f"Compare B: {b_name}, a {b_description}, from {b_country}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    followers_comparison = comparing(a_follower, b_follower)
    
    if guess == followers_comparison:
        count += 1
        print(f"Bingo! You're right! Current score: {count}")
        
        if followers_comparison == "a":
            b = compare()
            b_name, b_follower, b_description, b_country = players(b)
            while b == a:  # Avoid duplicates
                b = random.choice(data)
        
        else:
            a = compare()
            a_name, a_follower, a_description, a_country =players(a)
            while b == a:  # Avoid duplicates
                b = random.choice(data)
            
    else:
        print(f"Sorry! that's a wrong answer. Final score {count}")
        live_game = False