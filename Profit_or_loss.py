selling_price= int(input("Enter the selling price of the oranges- "))
cost_price= int(input("Enter the cost price of the oranges- "))
calculation= cost_price - selling_price
if cost_price > selling_price:
    print(f"Loss- {calculation}")
else:
    print(f"Profit {calculation}")