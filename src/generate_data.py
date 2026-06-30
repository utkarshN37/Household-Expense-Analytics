import csv
import random
from datetime import datetime, timedelta

members = ["Father", "Mother", "Sister", "Utkarsh"]

payment_modes = ["Cash", "UPI", "Card"]

# Weighted categories for realistic behavior
member_categories = {
    "Father": ["Bills", "Food", "Travel", "Bills", "Food"],
    "Mother": ["Shopping", "Food", "Shopping", "Food"],
    "Sister": ["Shopping", "Food", "Entertainment"],
    "Utkarsh": ["Gym", "Entertainment", "Food", "Gym"]
}

start_date = datetime(2026, 1, 1)

with open("expenses.csv", "w", newline="") as file:

    fieldnames = [
        "member_name",
        "category",
        "amount",
        "date",
        "payment_mode"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for _ in range(500):

        member = random.choice(members)

        category = random.choice(member_categories[member])

        amount = random.randint(50, 3000)

        payment_mode = random.choice(payment_modes)

        random_days = random.randint(0, 180)

        expense_date = (
            start_date + timedelta(days=random_days)
        ).strftime("%Y-%m-%d")

        expense = {
            "member_name": member,
            "category": category,
            "amount": amount,
            "date": expense_date,
            "payment_mode": payment_mode
        }

        writer.writerow(expense)

print("500 rows generated successfully!")