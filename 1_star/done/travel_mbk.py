# พี่เติ้ลอยากไปเที่ยว MBK อะโดยที่พี่จะเลือกเดินทางด้วยวิธีที่แพงที่สุดเพราะเร็วที่สุดแต่พี่มีงบจำกัดอยู่
# เพราะงั้นน้องๆช่วยบอกพี่หน่อยว่าพี่จะเดินทางด้วยอะไร

# ****โดยมีวิธีเดินทางดังนี้****

# Taxi : 50 บาท
# BTS : 40 บาท
# Motorcycle : 25 บาท
# Song Thaeo : 8 บาท
# แต่ BTS กับ Song Thaeo ไม่สามารถไปส่งถึง MBK ได้ ทำให้ต้องเดินทางต่อเองและแสดงข้อความ “walking” ถ้าไม่ใช่ ให้แสดงข้อความ “no walking” และในกรณีที่ไม่มีเงินออกเดินทางให้แสดงว่า “stay home”

budget = float(input())
if budget >= 50:
    print("Taxi")
    print("no walking")
elif budget >= 40: 
    print("BTS")
    print("walking")
elif budget >= 25:
    print("Motorcycle")
    print("no walking")
elif budget >= 8:
    print("Song Thaeo")
    print("walking")
else:
    print("stay home")