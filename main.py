
import csv
from pathlib import Path

file_path = Path("data/orders.csv")

# Read CSV
with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    orders = list(reader)
print("CSV Columns:", list(orders[0].keys()))

print("Total Original Records:", len(orders))

# Data Cleaning
clean_orders = []
seen_ids = set()

for order in orders:

    order_id = int(order["order_id"])
    quantity = int(order["quantity"])
    price = float(order["price"])

    # Remove duplicate orders
    if order_id in seen_ids:
        continue

    # Validate data
    if quantity <= 0 or price < 0:
        continue

    seen_ids.add(order_id)
    clean_orders.append(order)

# Save Clean Data
output_file = Path("data/clean_orders.csv")

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=orders[0].keys()
    )

    writer.writeheader()
    writer.writerows(clean_orders)

print("Clean Records:", len(clean_orders))
print("Removed Records:", len(orders) - len(clean_orders))
print("Data Cleaning Completed!")
