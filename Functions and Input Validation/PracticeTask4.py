def getData():
    prices = []
    total_price = 0
    highest_price = 0

    while True:
        try:
            cost = int(input("Enter the cost of the item: "))

            if cost <= 0:
                print("Error. Cost must be positive.")
                continue

            prices.append(cost)
            total_price += cost

            if cost > highest_price:
                highest_price = cost

        except ValueError:
            print("Recording stopped.")
            break

    if len(prices) > 0:
        if highest_price >= 200:
            discount = highest_price * 0.10
            discounted_price = highest_price - discount
        else:
            discount = 0
            discounted_price = highest_price

        print("Summary")
        print("Total cost:", total_price)
        print("Highest item cost:", highest_price)
        print("Discount amount:", discount)
        print("Cost after discount:", discounted_price)
    else:
        print("No valid items entered.")

getData()