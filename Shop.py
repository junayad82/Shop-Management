products = []
customers = []

while True:
    print("\n====== SHOP MANAGEMENT SYSTEM ======")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Sell Product")
    print("6. Add Customer")
    print("7. View Customers")
    print("8. Generate Bill")
    print("9. Save Data")
    print("10. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Product
    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        product = {
            "name": name,
            "price": price,
            "stock": stock
        }

        products.append(product)

        print("Product added successfully!")

    # 2. View Products
    elif choice == "2":
        if len(products) == 0:
            print("No products found!")
        else:
            print("\n====== PRODUCTS ======")

            for product in products:
                print(f"Product Name: {product['name']}")
                print(f"Price: {product['price']}")
                print(f"Stock: {product['stock']}")
                print("----------------------")

    # 3. Search Product
    elif choice == "3":
        search = input("Enter product name: ")
        found = False

        for product in products:
            if search.lower() == product["name"].lower():
                print("\nProduct Found!")
                print(f"Product Name: {product['name']}")
                print(f"Price: {product['price']}")
                print(f"Stock: {product['stock']}")

                found = True
                break

        if not found:
            print("Product not found!")

    # 4. Update Product
    elif choice == "4":
        search = input("Enter product name to update: ")
        found = False

        for product in products:
            if search.lower() == product["name"].lower():

                print("\nWhat do you want to update?")
                print("1. Price")
                print("2. Stock")
                print("3. Both")

                update_choice = input("Enter your choice: ")

                if update_choice == "1":
                    new_price = float(input("Enter new price: "))
                    product["price"] = new_price
                    print("Price updated successfully!")

                elif update_choice == "2":
                    new_stock = int(input("Enter new stock: "))
                    product["stock"] = new_stock
                    print("Stock updated successfully!")

                elif update_choice == "3":
                    new_price = float(input("Enter new price: "))
                    new_stock = int(input("Enter new stock: "))

                    product["price"] = new_price
                    product["stock"] = new_stock

                    print("Price and stock updated successfully!")

                else:
                    print("Invalid choice!")

                found = True
                break

        if not found:
            print("Product not found!")

    # 5. Sell Product
    elif choice == "5":
        search = input("Enter product name: ")
        found = False

        for product in products:
            if search.lower() == product["name"].lower():

                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Invalid quantity!")

                elif quantity > product["stock"]:
                    print("Not enough stock!")

                else:
                    total = product["price"] * quantity
                    product["stock"] -= quantity

                    print("Product sold successfully!")
                    print(f"Product: {product['name']}")
                    print(f"Quantity: {quantity}")
                    print(f"Total price: {total}")

                found = True
                break

        if not found:
            print("Product not found!")

    # 6. Add Customer
    elif choice == "6":
        name = input("Enter customer name: ")

        customer = {
            "name": name
        }

        customers.append(customer)

        print("Customer added successfully!")

    # 7. View Customers
    elif choice == "7":
        if len(customers) == 0:
            print("No customers found!")

        else:
            print("\n====== CUSTOMERS ======")

            for customer in customers:
                print(f"Customer Name: {customer['name']}")
                print("----------------------")

    # 8. Generate Bill
    elif choice == "8":
        customer_name = input("Enter customer name: ")

        found = False

        for customer in customers:
            if customer_name.lower() == customer["name"].lower():
                found = True
                break

        if not found:
            print("Customer not found!")

        else:
            print("\n====== BILL ======")
            print(f"Customer: {customer_name}")
            print("----------------------")

            total_bill = 0

            while True:
                product_name = input(
                    "Enter product name (or 'done' to finish): "
                )

                if product_name.lower() == "done":
                    break

                product_found = False

                for product in products:
                    if product_name.lower() == product["name"].lower():

                        quantity = int(input("Enter quantity: "))

                        if quantity <= 0:
                            print("Invalid quantity!")

                        elif quantity > product["stock"]:
                            print("Not enough stock!")

                        else:
                            subtotal = product["price"] * quantity

                            total_bill += subtotal

                            print(
                                f"{product['name']} x {quantity} = {subtotal}"
                            )

                        product_found = True
                        break

                if not product_found:
                    print("Product not found!")

            print("----------------------")
            print(f"Total Bill: {total_bill}")
            print("======================")

    # 9. Save Data
    elif choice == "9":
        with open("shop.txt", "w") as file:

            file.write("====== PRODUCTS ======\n")

            for product in products:
                file.write(f"Product Name: {product['name']}\n")
                file.write(f"Price: {product['price']}\n")
                file.write(f"Stock: {product['stock']}\n")
                file.write("----------------------\n")

            file.write("\n====== CUSTOMERS ======\n")

            for customer in customers:
                file.write(f"Customer Name: {customer['name']}\n")
                file.write("----------------------\n")

        print("Data saved successfully!")

    # 10. Exit
    elif choice == "10":
        print("Thank you for using Shop Management System!")
        break

    else:
        print("Invalid choice!")