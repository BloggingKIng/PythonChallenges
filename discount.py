prices = {'apple':4.00, 'oranges':9.00, 'bananas': 8, 'strawberries':20.00}

# give 25% discount on all fruits

for key, values in prices.items():
    price = values
    discount =  values * 0.25
    discounted_price = price - discount
    print("Discounted price of {} is {}".format(key, discounted_price))

    prices[key] = discounted_price


print(prices)