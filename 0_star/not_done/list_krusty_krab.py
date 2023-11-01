# แต่ละบรรทัดประกอบด้วยชื่ออาหาร และหมายเลขคอส คั่นด้วย " #" หากหมายเลขเมนูเป็น #N ให้ต่อท้ายสุดของเมนูในขณะนั้น หากเป็น จำนวนเต็มบวก ให้แทรกไปในตำแหน่งนั้น (เริ่มนับจาก 1)

menu_insert, menu_list, last_menu = [], [], []
while True:
    menu = input()
    if menu == "":
        continue
    if menu.lower() == 'done':
        break
    menu_split = menu.rsplit(" #")
    if len(menu_split) < 2:
        continue

    menu_name, menu_type = menu_split[0], menu_split[1].lower()
    if menu_type == 'n':
        last_menu = [menu_name]
    else:
        menu_list.append((menu_name, menu_type))

menu_list_sorted = sorted(menu_list, key=lambda x: (x[1], x[0]))
loop_menu_sorted = [i[0] for i in menu_list_sorted]
menu_result = loop_menu_sorted + last_menu
print(f"Menu: {menu_result}")