total_balance=0

def balance():
    print(f"Toatl balance:{total_balance}")

def deposit_money(amnt):
    if amnt>0:
        global total_balance
        total_balance +=amnt
        balance()
    else: print("provide valid amount")
    
def withdraw_money(amnt):
    if amnt>0:
        global total_balance
        total_balance -=amnt
        balance()
    else: print("provide valid amount")
    
balance()
dm=int(input("enter deposit money"))
wm=int(input("enter deposit money"))
deposit_money(dm)
withdraw_money(wm)
