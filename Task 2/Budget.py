import json
from collections import defaultdict

def load_data():
    try:
        with open('budget_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': 0, 'expenses': []}

def save_data(data):
    with open('budget_data.json', 'w') as file:
        json.dump(data, file)

def add_income(data):
    income = float(input("Enter income amount: "))
    data['income'] += income
    print(f"Income of ${income} added successfully.")

def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})
    print(f"Expense of ${amount} in category '{category}' added successfully.")

def calculate_budget(data):
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - total_expenses
    print(f"Remaining Budget: ${remaining_budget}")

def expense_analysis(data):
    categories = defaultdict(float)
    for expense in data['expenses']:
        categories[expense['category']] += expense['amount']

    print("Expense Analysis:")
    for category, amount in categories.items():
        print(f"{category}: ${amount}")

def main():
    budget_data = load_data()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_income(budget_data)
        elif choice == '2':
            add_expense(budget_data)
        elif choice == '3':
            calculate_budget(budget_data)
        elif choice == '4':
            expense_analysis(budget_data)
        elif choice == '5':
            save_data(budget_data)
            print("Exiting Budget Tracker. Data saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
