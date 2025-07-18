import random
import datetime
import json
import os

FRIENDS_FILE = "friends.json"
STATS_FILE = "stats.json"


def load_friends():
    if os.path.exists(FRIENDS_FILE):
        with open(FRIENDS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Choose from the Menu 🔖.")
                return []
    return []

def save_friends(friends):
    with open(FRIENDS_FILE, "w") as file:
        json.dump(friends, file)

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Choose from the Menu 🔖")
                return {}
    return {}

def save_stats(stats):
    with open(STATS_FILE, "w") as file:
        json.dump(stats, file)

def fun_message(name):
    messages = [
        f"Oh no, {name}! Your wallet cries again! 🥲",
        f"{name}, it’s your lucky day... or not! 😂",
        f"{name} will pay! Generous soul alert! 💸",
        f"{name}, better luck next time! 🍽️",
        f"Guess what? {name} is treating us today! 🎉"
    ]
    return random.choice(messages)

def view_friends(friends):
    if not friends:
        print("\nFriend list is empty.")
    else:
        print("\nCurrent Friends:")
        for idx, friend in enumerate(friends, 1):
            print(f"{idx}. {friend}")

def remove_friend(friends, stats):
    view_friends(friends)
    if not friends:
        return friends, stats

    name_to_remove = input("\nEnter the name of the friend to remove: ")
    if name_to_remove in friends:
        friends.remove(name_to_remove)
        if name_to_remove in stats:
            del stats[name_to_remove]
        save_friends(friends)
        save_stats(stats)
        print(f"{name_to_remove} has been removed from the group.")
    else:
        print("Friend not found.")

    return friends, stats

def add_friends(friends, stats):
    while True:
        name = input("Enter a friend's name (or type 'done' to finish): ").strip()
        if name.lower() == "done":
            if friends:
                save_friends(friends)
                save_stats(stats)
                break
            else:
                print("You must add at least one friend.")
        elif not name:
            print("Name cannot be empty.")
        elif name in friends:
            print(f"{name} is already in the list.")
        else:
            friends.append(name)
            stats[name] = 0
            print(f"{name} added!")

# ---------- Main Program ----------
print("Welcome to 'Who Will Pay the Bill?'🤔")

friends = load_friends()
stats = load_stats()

# First-time user prompt
if not friends:
    print("\n👋 It looks like you're a new user. No friends found.")
    choice = input("Would you like to add friends now? (yes/no): ").strip().lower()
    if choice == "yes":
        add_friends(friends, stats)

# Main menu loop
while True:
    print("\n--- Menu ---")
    print("1. Add a New Friend ")
    print("2. Start Bill Split")
    print("3. Remove Friend")
    print("4. View Friend List")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "2":
        if not friends:
            print("Friend list is empty. Add friends first.")
            continue

        print("\nCurrent Group:")
        print(", ".join(friends))

        exclude = input("\nIs there someone to exclude from paying? (yes/no): ").lower()
        excluded_person = None
        if exclude == "yes":
            person_to_exclude = input("Enter the name of the person to exclude: ")
            if person_to_exclude in friends:
                excluded_person = person_to_exclude
                print(f"{excluded_person} is excluded from paying today! 🎂")
            else:
                print("Name not found. No one will be excluded.")

        eligible_friends = [f for f in friends if f != excluded_person]

        if not eligible_friends:
            print("No one is left to pay the bill. Returning to menu.")
            continue

        # Ensure stats entries
        for friend in eligible_friends:
            if friend not in stats:
                stats[friend] = 0

        while True:
            bill_input = input("\nEnter the total bill amount (₹): ")
            try:
                bill_amount = float(bill_input)
                if bill_amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    break
            except ValueError:
                print("Invalid number. Try again.")

        print("\nHow do you want to pay?")
        print("1. Pick one person to pay the whole bill.")
        print("2. Split the bill equally between eligible friends.")

        while True:
            option = input("Choose option 1 or 2: ")
            if option not in ["1", "2"]:
                print("Invalid choice. Please select 1 or 2.")
            else:
                break

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if option == "1":
            min_pays = min(stats[f] for f in eligible_friends)
            least_payers = [f for f in eligible_friends if stats[f] == min_pays]
            bill_payer = random.choice(least_payers)

            print("\n" + fun_message(bill_payer))
            print(f"{bill_payer} will pay ₹{bill_amount} today! 🍽️")

            stats[bill_payer] += 1

            with open("payment_history.txt", "a", encoding="utf-8") as file:
                file.write(f"{now} - {bill_payer} paid ₹{bill_amount}\n")

        else:
            share = round(bill_amount / len(eligible_friends), 2)
            print(f"\nEach person will pay ₹{share}")

            for person in eligible_friends:
                stats[person] += 1

            with open("payment_history.txt", "a", encoding="utf-8") as file:
                for person in eligible_friends:
                    file.write(f"{now} - {person} paid ₹{share}\n")

        save_stats(stats)
        print("\n✅ Payment recorded in 'payment_history.txt'.")

        print("\n--- Payment Statistics ---")
        for friend in stats:
            print(f"{friend}: {stats[friend]} times paid")

    elif choice == "1":
        add_friends(friends, stats)

    elif choice == "3":
        friends, stats = remove_friend(friends, stats)

    elif choice == "4":
        view_friends(friends)

    elif choice == "5":
        print("Exiting. Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please enter 1-5.")
