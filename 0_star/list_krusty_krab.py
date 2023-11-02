# แต่ละบรรทัดประกอบด้วยชื่ออาหาร และหมายเลขคอส คั่นด้วย " #" หากหมายเลขเมนูเป็น #N ให้ต่อท้ายสุดของเมนูในขณะนั้น หากเป็น จำนวนเต็มบวก ให้แทรกไปในตำแหน่งนั้น (เริ่มนับจาก 1)

# menu_insert, menu_list, n_menu = [], [], []
# while True:
#     menu = input()
#     if menu == "":
#         continue
#     if menu.lower() == 'done':
#         break
#     menu_split = menu.rsplit(" #")
#     if len(menu_split) < 2:
#         continue

#     menu_name, menu_type = menu_split[0], menu_split[1].lower()
#     if menu_type == 'n':
#         n_menu = [menu_name]
#     else:
#         menu_list.append((menu_name, menu_type))

# menu_list_sorted = sorted(menu_list, key=lambda x: (x[1], x[0]))
# loop_menu_sorted = [i[0] for i in menu_list_sorted]
# menu_result = loop_menu_sorted + n_menu
# print(f"Menu: {menu_result}")

menu_list = []

while True:
    menu_input = input()
    if menu_input.lower() == 'done':
        break

    menu_parts = menu_input.rsplit(" #")
    if len(menu_parts) < 2:
        continue

    menu_name, menu_type = menu_parts[0], menu_parts[1].lower()

    if menu_type == "n":
        menu_list.append(menu_name)
    else:
        menu_position = int(menu_type) - 1
        if menu_position < 0:
            menu_position = 0
        elif menu_position > len(menu_list):
            menu_position = len(menu_list)
        menu_list.insert(menu_position, menu_name)

print("Menu:", menu_list)