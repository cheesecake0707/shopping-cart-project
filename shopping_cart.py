# shopping_cart.py

selected_ids = []
all_ids = []

import csv
csv_file_path = "data/products.csv" #file path in folder

while True:
    selected_id = input("PLEASE INPUT A PRODUCT IDENTIFIER: ")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ids in reader:
            all_ids.append(ids["id"])
        if selected_id == "DONE":
            break
        elif selected_id not in all_ids:
            print("SOMETHING WENT WRONG, PLEASE TRY AGAIN")
            exit()
        else:
                selected_ids.append(selected_id)

def to_usd(my_price):
    return "${:,.2f}".format(my_price)


#name/website
print("----------------------------------------------------")
print("ORGANIC GREEN GROCERY")
print("WWW.ORGANIC-GREEN-GROCERY.COM")

#date/time
print("----------------------------------------------------")

import time
today = time.strftime('%l:%M%p %Z on %b %d, %Y')
print("CHECKOUT AT:", today)

#outputs - products
print("----------------------------------------------------")

subtotal_price = 0

print("SELECTED PRODUCTS:")

import csv
csv_file_path = "data/products.csv" #file path in folder
for selected_id in selected_ids:
    with open(csv_file_path, "r") as csv_file: #need to solve loop with multiple items
        reader = csv.DictReader(csv_file)
        matching_products = [p for p in reader if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        subtotal_price = subtotal_price + (float(matching_product["price"]))
        print("..." + matching_product["name"] + " (" + to_usd(float(matching_product["price"])) + ")")

#inputs&outputs - tax, subtotal and total
print("---------------------------------")
print("SUBTOTAL: " + to_usd(subtotal_price))

tax_rate = 0.0875 #nyc tax rate
tax = subtotal_price * tax_rate
print("TAX: " + to_usd(tax))

total_price = subtotal_price + tax
print("TOTAL: " + to_usd(total_price))

#thank you message
print("----------------------------------------------------")
print("THANK YOU!  PLEASE COME AGAIN")
print("----------------------------------------------------")