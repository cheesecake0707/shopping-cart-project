# shopping_cart.py

#name/website
print("----------------------------------------------------")

print("ORGANIC GREEN GROCERY")
print("WWW.ORGANIC-GREEN-GROCERY.COM")

#date/time
print("----------------------------------------------------")

import time
today = time.strftime('%l:%M%p %Z on %b %d, %Y')
print("CHECK OUT AT:", today)

#inputs&outputs
print("----------------------------------------------------")

import csv

csv_file_path = "data/products.csv" #file path in my folder

while True:
    with open(csv_file_path, "r") as csv_file: #need to solve loop with multiple items
        reader = csv.DictReader(csv_file)
        selected_id = input("PLEASE INPUT A PRODUCT IDENTIFIER: ")
        if selected_id == "DONE":
            break
        else:
            matching_product = [p for p in reader if str(p["id"]) == str(selected_id)]
            matching_products = matching_product[0]
            print("SELECTED PRODUCT: " + matching_products["name"] + " " + str(matching_products["price"]))


#total_price = 0
#print("TOTAL PRICE: " + str(total_price))



#thank you message
#print("----------------------------------------------------")
#print("THANK YOU!  PLEASE COME AGAIN")
