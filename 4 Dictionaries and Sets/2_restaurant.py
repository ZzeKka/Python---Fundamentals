MENU = {
    'picapau' : 50,
    'bacalhau' : 45,
    'doradinhos' : 20,
    'bitoque' : 35
}

def menu_order():
    total = 0
    order = 'nothing'
    while order != '':
        order = input("What would you like to order? ").strip()
        if order in MENU:
            total += MENU[order]
            print(f"{order} price: {MENU[order]}$\nTotal: {total}$")
        else:
            print(f"plz enter an order available in the menu, dumass")
    print(f"Dont run! Pay {total}$ right now!")
        
menu_order()