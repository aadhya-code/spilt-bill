
# 🧾 Who Will Pay the Bill? – Python App

A fun and simple command-line Python app that helps you decide who will pay the bill in a group of friends! You can either split the bill equally or randomly select one person to pay (based on fairness).

---

## 📦 Features

- ➕ Add and manage friends
- 🎯 Randomly pick a person to pay the bill (fair selection)
- ⚖️ Split the bill equally among group members
- ❌ Exclude a friend from paying (e.g., birthday, special occasion)
- 📈 Track how many times each friend has paid
- 🧾 Automatically save payment history to a text file
- 📂 Stores data persistently using JSON files

---

## 📁 Files

| File                  | Purpose                                      |
|-----------------------|----------------------------------------------|
| `splitbill.py`        | Main Python program                          |
| `friends.json`        | Stores the list of friends                   |
| `stats.json`          | Stores how many times each friend has paid   |
| `payment_history.txt` | Logs all past payments                       |
| `README.md`           | This documentation file                      |

---

## ▶️ How to Run

1. Make sure you have **Python 3 installed**.
2. Place `splitbill.py` in your working folder.
3. Open your terminal and run:

bash
python3 splitbill.py

Welcome to 'Who Will Pay the Bill?'🤔

👋 It looks like you're a new user. No friends found.
Would you like to add friends now? (yes/no): yes
Enter a friend's name (or type 'done' to finish): Alice
Alice added!
Enter a friend's name (or type 'done' to finish): Bob
Bob added!
Enter a friend's name (or type 'done' to finish): done

--- Menu ---
1. Add a New Friend 
2. Start Bill Split
3. Remove Friend
4. View Friend List
5. Exit
