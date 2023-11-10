# พี่มีเกม MOBA บนคอมอยู่เกมนึงชื่อ LOL พี่เพิ่งหัดเล่นโดยที่พี่เล่นกับพี่มอสเขาจะเล่นตำแหน่ง Support เสมอ ส่วนพี่จะเล่นตำแหน่งอื่นๆที่เหลือเองเพราะพี่อยากลองฝึกดู
# ทีนี้เริ่มเกมพี่จะมีเงินอยู่ 500 Gold และพี่จะซื้อของต้นเกมเลย เอาละน้องๆจะได้รับหน้าที่เป็นพี่มอสโดยพี่มอสจะเตือนพี่ว่าพี่ต้องซื้อ item อะไรที่ยังขาดอยู่พร้อมบอกเงินที่พี่เหลืออยู่
# ถ้าพี่ออกผิดพี่มอสจะบอกชิ้นที่ถูกด้วย

# item ตามตำแหน่งมีดังนี้
# Tank : Doran Shield(450 Gold) , Health Potion(50 Gold)
# Mage : Doran Ring(400 Gold) , Health Potion(50 Gold) , Health Potion(50 Gold)
# ADC : Doran Blade(450 Gold) , Health Potion(50 Gold)
# Fighter : Doran Blade(450 Gold) , Health Potion(50 Gold)
# ตำแหน่งป่าจะถูกแบ่งเป็น 2 สายคือ AD และ AP
# โดยพี่จะบอกมอสก่อนว่าพี่จะเล่น AD หรือ AP

# Jungle(AD) : Hunter's Machete(350 Gold) , Refillable Potion(150 Gold)
# Jungle(AP) : Hunter's Talisman(350 Gold) , Refillable Potion(150 Gold)
# **ถ้าพี่ซื้อ item ถูกอยู่แล้วพี่มอสจะพูดว่า Perfect

# Input Specification
# n บรรทัด
# ตำแหน่งที่พี่เล่น
# AD หรือ AP หากเล่น Jungle
# n item ที่พี่ต้องการซื้อ
# n+1 END(หยุดการซื้อของ)

# Output Specification
# 1 บรรทัด
# Perfect ถ้าพี่ซื้อ item ตรงตามตำแหน่ง
# ไอเทมที่พี่ต้องซื้อหรือขาดอยู่ พร้อมเงินที่เหลืออยู่

item = {
    "tank" : (
        "Doran Shield" : 450,
        "Health Potion" : 50,
    ),
    "mage" : (

    ),
}