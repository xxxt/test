amount = float(input("Enter amount:"))
inrate = float(input("Enter intare:"))
period = int(input("Enter perbiod:"))

value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year{} Rs. {:.3f}".format(year,value))
    amount = value
    year += 1
