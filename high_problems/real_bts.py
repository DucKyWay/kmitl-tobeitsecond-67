# https://www.bts.co.th/routemap.html
# https://www.youtube.com/watch?v=xwq45th06Nw

# N8- E9, W1 - S6 --> 17 25 28 32 35 40 43 47 สัมปทานหลัก
# S6 - S8 ให้เก็บค่าโดยสารร่วมกับส่วนสัมปทานหลัก
# E9 - E14 --> 15 บาท กรุงเทพมหานคร
# S8 - S12 --> 15 บาท กรุงเทพมหานคร
# E14 - E23 ฟรี
# N8 - N24 ฟรี

# ถ้านั่งข้ามส่วน เช่น E4 - E10 จะโดนค่าโดยสารทั้งหมด 2 ส่วน คือ ส่วนสัมปทานหลัก และ ส่วนของกรุงเทพมหานคร
# N6 "Error"

BKK_normal = [17, 17, 25, 28, 32, 35, 40, 43, 47]
BMA_flat_fare = 15
n_list = [f'N{i}' for i in range(1, 25)]
e_list = [f'E{i}' for i in range(1, 24)]
w_list = ['W1']
s_list = [f'S{i}' for i in range(1, 13)]
center_list = ['CEN']
station_list = n_list + center_list + e_list + w_list + s_list
free_n = [f'N{i}' for i in range(9, 25)]
free_e = [f'E{i}' for i in range(14, 24)]

def calculate_fare(entrance, terminal):
    if entrance == station_list and terminal == station_list:
        if entrance == "N6" or terminal == "N6":
            return "Error"

        if (entrance in free_n and terminal in free_n) or \
        (entrance in free_e and terminal in free_e):
            return 0
        
        main_fare = 0
        if "N" in entrance and "N" in terminal:
            for i in range(station_entrance, station_terminal):
                calc_price = BKK_normal[i]
                return calc_price

        elif "E" in entrance and "E" in terminal:
            print("E")

        elif "W" in entrance and "W" in terminal:
            print("W")

        elif "S" in entrance and "S" in terminal:
            print("S")
        
        bma_fare = 0


entrance, terminal = input(), input()

station_entrance = ''.join([i for i in entrance if i.isdigit()])
station_terminal = ''.join([i for i in terminal if i.isdigit()])

price = calculate_fare(entrance, terminal)
print(price)
