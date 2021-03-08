import ecommerce as e

# Adding a new customers - (name, email)
customer_joe = e.Customer('Joe', 'joe@gmail.com')
customer_martin = e.Customer('Martin', 'martin@hotmail.com')
customer_dayana = e.Customer('Dayana','dayana@hotmail.com')

# Adding products - (product, price)
apple_watch = e.Product('Apple Watch', 299)
mac_2020 = e.Product('Macintosh 2020', 1999)
airpods_v2 = e.Product('New Airpods', 129)
airpods_pro = e.Product('Airpods Pro', 199)
iphone_12_pro = e.Product('iPhone 12 Pro',1099)

# Creating and inventory object
inventory = e.Inventory()

# Adding products to the inventory (.product, quantity)
inventory.add_product(apple_watch, 100)
inventory.add_product(mac_2020, 498)
inventory.add_product(airpods_v2, 1200)
inventory.add_product(airpods_pro, 450)
inventory.add_product(iphone_12_pro, 200)

# Printing the current inventory
inventory.print_inventory()

# Customer making a purchase
customer_martin.purchase(inventory, apple_watch)
customer_martin.purchase(inventory, mac_2020)

# Printing the current inventory after a purchase
inventory.print_inventory()

# Printing Customer's purchase history
customer_martin.print_purchases()
