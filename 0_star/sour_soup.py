def main():

    menu_dic = {
        "shrimp sour soup": 80,
        "mixed vegetables sour soup": 60,
    }

    total = 0
    while True:
        menu = str(input())
        if menu == "stop":
            break
        total += num

    print(total)
main()


# ร้านแกงส้มร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าซื้อแกงส้มมากกว่าหรือเท่ากับ 3 ถุง
# และมีมูลค่ารวมตั้งแต่ 200 บาทขึ้นไป ลูกค้าจะได้ส่วนลด 15% โดยราคาของแกงส้มคือ

# shrimp sour soup (แกงส้มกุ้ง) 80 บาท
# mixed vegetables sour soup (แกงส้มผักรวม) 60 บาท
# papaya sour soup (แกงส้มมะละกอ) 55 บาท
# snapper fish sour soup (แกงส้มปลากะพง) 100 บาท
# cha om shrimp sour soup (แกงส้มชะอมกุ้ง) 100 บาท
# Input Specification
# N บรรทัด

# บรรทัดที่ 1 ชื่อแกง
# บรรทัดที่ N ใส่ stop เพื่อจบการทำงาน
# Output Specification
# 3 บรรทัด

# บรรทัดที่ 1 ราคาเต็ม คือ ราคาเดิมที่ยังไม่หักส่วนลด (จำนวนเต็ม)
# บรรทัดที่ 2 ส่วนลด คือ ส่วนลดที่หักไป (จำนวนเต็ม)
# บรรทัดที่ 3 ราคาสุทธิ คือ ราคาเต็มที่หักส่วนลดแล้ว (จำนวนเต็ม)

# Original Price 200 baht
# Discount 0 baht
# Total 200 baht