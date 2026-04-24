# expense_tracker.py
import json
import os

FILE = "expenses.json"

def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    name = input("What did you spend on? ")
    amount = float(input("How much? ₹ "))
    expenses.append({"name": name, "amount": amount})
    save_expenses(expenses)
    print(f"✓ Added ₹{amount} for {name}\n")

def show_total(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"\n📊 Total spent: ₹{total}")
    for e in expenses:
        print(f"  - {e['name']}: ₹{e['amount']}")

expenses = load_expenses()
while True:
    print("1. Add expense  2. View total  3. Quit")
    choice = input("Choose: ")
    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        show_total(expenses)
    elif choice == "3":
        break