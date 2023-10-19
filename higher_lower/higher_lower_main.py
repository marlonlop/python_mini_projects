from art import logo, vs
from data import data
import random
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_data(account):
    """takes the acct data and returns the printable format"""
    acct_name = account['name']
    acct_descr = account['description']
    acct_country = account['country']
    return f"{acct_name}, a {acct_descr}, from {acct_country}"

def check_answer(guess, a_followers, b_followers):
    """Check if answer is correct"""
    '''
    if guess == "a":
        if a_followers > b_followers:
            return True
        else: return False
    if guess == "b":
        if a_followers < b_followers:
            return True
        else: return False
    '''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
print(logo)
account_b = random.choice(data)

while(True):

    # picking both accounts
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # get guess
    exp_ans = ('a', 'b')
    guess = ""
    while guess not in exp_ans:
        guess = input("Who has more followers? type A or B: ").lower()
        if guess not in exp_ans:
            if guess == "exit" or guess == "x": 
                print("exiting") 
                exit(0)
            print("I said A or B")

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    cls()
    print(logo)

    if is_correct:
        score += 1
        print(f"Right, current score: {score}")
    else:
        print(f"Wrong, final score: {score}")
        print("exiting") 
        exit(0)