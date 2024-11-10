def sales(price, rate):
    sales_tax = price + (price*(rate/100))

    total = price + sales_tax
    return sales_tax, total



