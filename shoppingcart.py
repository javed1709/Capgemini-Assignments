list=[]
total_price=0
def additems(name,price):
    global list
    list.append((name,price))
    global total_price
    total_price +=price
def viewcart():
    print("Total items")
    for i in list:
        print(i)

while True:
    choice=int(input("Enter choice of action:\n 1.To add items to cart\n 2.To viewcart items\n 3.See total price\n 4.Exit\n"))
    if choice==1:
        item=input("Enter the item:")
        price=int(input("Enter the price of item:"))
        additems(item,price)
    elif choice==2:
        viewcart()
    elif choice==3:
        # global total_price
        print(f"Total price of all items is:{total_price}")
    elif choice==4:
        break

