menu_dic = {
    "shrimp sour soup": 80,
    "mixed vegetables sour soup": 60,
    "papaya sour soup": 55,
    "snapper fish sour soup": 100,
    "cha om shrimp sour soup": 100
}
total, count, sale_price, sale = 0, 0, 0, 0
order = []
while True:
    menu = input()
    if menu == "stop":
        break
    if menu in menu_dic:
        order.append(menu)
        total += menu_dic[menu]
        count += 1
    
if count >= 3 and total >= 200:
    sale_price = total * 0.85
    sale = total - sale_price
else:
    sale_price = total

print(f'Original Price {total} baht')
print(f'Discount {int(sale)} baht')
print(f'Total {sale_price:.0f} baht')