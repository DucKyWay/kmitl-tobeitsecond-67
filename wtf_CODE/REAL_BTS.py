# เราจะมาคิดค่าโดยสารของรถไฟฟ้า BTS แบบปัจจุบันกันดีกว่า (อ้างอิงจากเว็บ: https://www.bts.co.th/routemap.html)

# ส่วนสัมปทานเริ่มแรก ตั้งแต่สถานีหมอชิต (N8) ถึงสถานีอ่อนนุช (E9) ของสายสุขุมวิท และ สถานีสนามกีฬาแห่งชาติ (W1) ถึงสะพานตากสิน (S6) ของสายสีลม จำนวน 23 สถานี normal rate
# 17 25 28 32 35 40 43 47
# ส่วนต่อขยายสายสีลม ช่วงตากสิน - เพชรเกษม ระยะที่ 1 จากสถานีสะพานตากสิน (S6) ถึงสถานีวงเวียนใหญ่ (S8) จำนวน 2 สถานี ให้เก็บค่าโดยสารร่วมกับส่วนสัมปทานหลัก
# ส่วนต่อขยายสายสุขุมวิท ระยะที่ 1 ช่วงอ่อนนุช - แบริ่ง (ลาซาล) จากสถานีอ่อนนุช (E9) ถึงสถานีแบริ่ง (E14) จำนวน 5 สถานี ให้เก็บค่าโดยสารแบบเหมาจ่าย 15 บาท กรุงเทพมหานคร
# ส่วนต่อขยายสายสีลม ช่วงตากสิน - เพชรเกษม ระยะที่ 2 จากสถานีวงเวียนใหญ่ (S8) ถึงสถานีบางหว้า (S12) จำนวน 4 สถานี ให้เก็บค่าโดยสารแบบเหมาจ่าย 15 บาท กรุงเทพมหานคร เช่นเดียวกับส่วนต่อขยายสายสุขุมวิท ระยะที่ 1
# ส่วนต่อขยายสายสุขุมวิทใต้ (เขียวใต้) จากสถานีแบริ่ง (E14) ถึงสถานีเคหะฯ (E23) จำนวน 9 สถานี ดูแลโดยกรุงเทพมหานคร ช่วงนี้ฟรีค่าบริการ
# ส่วนต่อขยายสายสุขุมวิทเหนือ (เขียวเหนือ) จากสถานีหมอชิต (N8) ถึงสถานีคูคต (N24) จำนวน 16 สถานี ดูแลโดยกรุงเทพมหานคร ช่วงนี้ฟรีค่าบริการ เช่นเดียวกับส่วนต่อขยายสายสุขุมวิทใต้ (เขียวใต้)

# ข้อสังเกตในการเก็บค่าโดยสาร อ้างอิงจากเว็บไซต์ของรถไฟฟ้า BTS (https://www.bts.co.th/routemap.html)
# ถ้านั่งผ่านส่วนของกรุงเทพมหานคร ให้เก็บค่าโดยสารของส่วนกรุงเทพมหานครแค่ครั้งเดียว กรุงเทพมหานครไม่ได้ใจร้ายกับเราขนาดนั้น
# ถ้านั่งข้ามส่วน เช่น พี่นั่งจากสถานีอโศก (E4) ไปสถานีบางจาก (E10) พี่ก็จะโดนค่าโดยสารทั้งหมด 2 ส่วน คือ ส่วนสัมปทานหลัก และ ส่วนของกรุงเทพมหานคร เช่นเดียวกันกับส่วนอื่นๆ
# N6 "Error"
# https://www.youtube.com/watch?v=xwq45th06Nw

BKK_normal = [0, 17, 25, 28, 32, 40, 43, 47]
BMA_flat_fare = 15
free_service_stations = ['E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24']
free_N = ['N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24']
free_E = ['E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23']

free_stage = 0

def calculate_fare(entrance, terminal):
    if entrance == "N6" or terminal == "N6":
        return "Error"

    if (entrance in free_N and terminal in free_N) or \
       (entrance in free_E and terminal in free_E):
        return 0
    
    main_fare = 0

    if ("N" in entrance and "E" in terminal) or \
       ("E" in entrance and "N" in terminal):
        print("N - E")
        # main_fare = max(BKK_normal)

    elif ("N" in entrance and "S" in terminal) or \
         ("S" in entrance and "N" in terminal):
        print("N - S")

    elif ("N" in entrance and "W" in terminal) or \
         ("W" in entrance and "N" in terminal):
        print("N - W")

    elif ("S" in entrance and "W" in terminal) or \
         ("W" in entrance and "S" in terminal):
        print("S - W")

    elif ("S" in entrance and "E" in terminal) or \
         ("E" in entrance and "S" in terminal):
        print("S - E")

    elif ("E" in entrance and "W" in terminal) or \
         ("W" in entrance and "E" in terminal):
        print("E - W")
    
    # elif
    bma_fare = 0
    if entrance in free_service_stations and terminal not in free_service_stations or \
       entrance not in free_service_stations and terminal in free_service_stations:
        bma_fare = BMA_flat_fare

    total_fare = main_fare + bma_fare

    if entrance in free_service_stations or terminal in free_service_stations:
        total_fare += BMA_flat_fare
    
    return total_fare

entrance, terminal = input(), input()
price = calculate_fare(entrance, terminal)
print(price)
