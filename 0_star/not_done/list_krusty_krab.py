# Description
# ลูกค้าแต่ละคนต้องสั่งไม่ต่ำกว่า 1 ชนิด 

# Input Specification
# หลายบรรทัด รับไปเรื่อยๆจนกว่าจะเจอคำว่า "DONE"
# แต่ละบรรทัดประกอบด้วยชื่ออาหาร และหมายเลขคอส คั่นด้วย " #" หากหมายเลขเมนูเป็น #N ให้ต่อท้ายสุดของเมนูในขณะนั้น หากเป็น จำนวนเต็มบวก ให้แทรกไปในตำแหน่งนั้น (เริ่มนับจาก 1)

# Output Specification
# บรรทัดเดียวคือ เมนูของร้านนี้ทั้งตามลำดับเมนูแรกจนสุดท้าย (ตาม sample case)

# Krabby Patty #2
# Krabby Meal #1
# DONE
# Menu: ['Krabby Meal', 'Krabby Patty']

# menu_insert, menu_list = [], []
# while True:
#     menu = input()
#     if menu.lower() == 'done':
#         break
#     menu_insert = menu.rsplit(" #")
#     menu_list.append(menu_insert)
# menu_list_sorted = sorted(menu_list, key=lambda x: (int(x[1]), x[0]))
# menu_result = []
# for i in menu_list_sorted:
#     menu_result.append(i[0])
# print(f"Menu: {menu_result}")

menu_insert, menu_list = [], []
while True:
    menu = input()
    if menu.lower() == 'done':
        break
    menu_insert = menu.rsplit(" #")
    menu_list.append(menu_insert)
menu_list_sorted = sorted(menu_list, key=lambda x: (int(x[1]), x[0]))
menu_result = [i[0] for i in menu_list_sorted]
print(f"Menu: {menu_result}")
