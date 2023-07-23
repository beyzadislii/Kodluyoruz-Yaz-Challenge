cost=int(input("How much does a product cost?: "))
price=int(input("What will be the selling price of your product?: "))
          
if cost<=0:
    raise ValueError("Cost cannot be negative!")
if price<=0:
    raise ValueError("Price cannot be negative!")
if price<cost:
   raise ValueError("Price cannot be less than cost")
while True:
  try: 
     one_profit= price-cost
     piece= cost/one_profit
     print(f"You will start making profit after {piece} items are sold")
     break
     
  except ValueError():
     continue
  