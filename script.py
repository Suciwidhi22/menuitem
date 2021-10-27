from menu_item import MenuItem

menu_item1 = MenuItem('Ice Americano', 5)
menu_item2 = MenuItem('Ice Cofee latte', 7)
menu_item3 = MenuItem('Hot Matcha latte', 7)
menu_item4 = MenuItem('Ice Matcha Latte', 10)
menu_item5 = MenuItem('Hot Capuccino', 7)
menu_item6 = MenuItem('Ice Capuccino', 10)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4, menu_item5, menu_item6]
index = 0

for menu_item in menu_items :
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('Input Menu Number: '))
selected_menu = menu_items[order]
print('Choosen item: ' + selected_menu.name)

count = int(input('Order Quantity (10% discount for 3 or more): '))
result = selected_menu.get_total_price(count)

print('Total ' + str(result))
