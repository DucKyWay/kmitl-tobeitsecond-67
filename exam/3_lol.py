# มีเงินอยู่ 500 Gold และพี่จะซื้อของต้นเกมเลย เอาละน้องๆจะได้รับหน้าที่เป็นพี่มอสโดยพี่มอสจะเตือนพี่ว่าพี่ต้องซื้อ item อะไรที่ยังขาดอยู่พร้อมบอกเงินที่พี่เหลืออยู่
# ถ้าพี่ออกผิดพี่มอสจะบอกชิ้นที่ถูกด้วย **ถ้าพี่ซื้อ item ถูกอยู่แล้วพี่มอสจะพูดว่า Perfect

# Perfect ถ้าพี่ซื้อ item ตรงตามตำแหน่ง
# ไอเทมที่พี่ต้องซื้อหรือขาดอยู่ พร้อมเงินที่เหลืออยู่

item = {
    "Tank" : {
        "Doran Shield" : 450,
        "Health Potion" : 50,
    },
    "Mage" : {
        "Doran Ring" : 400,
        "Health Potion" : 50,
        "Health Potion" : 50,
    },
    "ADC" : {
        "Doran Blade" : 450,
        "Health Potion" : 50,
    },
    "Fighter" : {
        "Doran Blade" : 450,
        "Health Potion" : 50,
    },
    "Jungle" : {
        "AD" : {
            "Hunter's Machete" : 350,
            "Refillable Potion" : 150,
        },
        "AP" : {
            "Hunter's Talisman" : 350,
            "Refillable Potion" : 150,
        },
    },
}
money, buy_item, position_input, count_buy = 500, [], str(input()), 0
if position_input == "Jungle": jungle_position = str(input())

while True:
    buy_item.append(str(input()))
    if buy_item == "END": 
        buy_item.pop()
        break
    else:
        count_buy += 1

for i in range(count_buy):
    print(test)