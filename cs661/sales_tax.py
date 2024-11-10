def sales(price, rate):
    sales_tax = price + (price*(rate/100))

    total = price + sales_tax
    return sales_tax, total

price = 100
rate = 6.25
sales_tax, total = sales(price, rate)
print(f"{sales_tax}")
print(f"{total}")

