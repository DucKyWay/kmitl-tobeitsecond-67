# จะต้องเตือนพี่ว่าพี่ต้องซื้อ item อะไรที่ยังขาดอยู่พร้อมบอกเงินที่พี่เหลืออยู่ ถ้าพี่ออกผิดพี่มอสจะบอกชิ้นที่ถูกด้วย **ถ้าพี่ซื้อ item ถูกอยู่แล้วพี่มอสจะพูดว่า Perfect

# Perfect ถ้าพี่ซื้อ item ตรงตามตำแหน่ง
# ไอเทมที่พี่ต้องซื้อหรือขาดอยู่ พร้อมเงินที่เหลืออยู่

item = {
    "Tank": {"Doran Shield": 450, "Health Potion": 50},
    "Mage": {"Doran Ring": 400, "Health Potion": 50, "Health Potion": 50},
    "ADC": {"Doran Blade": 450, "Health Potion": 50},
    "Fighter": {"Doran Blade": 450, "Health Potion": 50},
    "Jungle": {
        "AD": {"Hunter's Machete": 350, "Refillable Potion": 150},
        "AP": {"Hunter's Talisman": 350, "Refillable Potion": 150},
    },
}

money, buy_item, count_buy = 500, [], 0
position_input = input().strip()
if position_input == "Jungle": jungle_position = input().strip()

while True:
    item_to_buy = input().strip()
    if item_to_buy == "END": break
    else:
        buy_item.append(item_to_buy)
        count_buy += 1

for item_to_buy in buy_item:
    if position_input == "Tank" and item_to_buy in item["Tank"]:
        money -= item["Tank"][item_to_buy]
    elif position_input == "Mage" and item_to_buy in item["Mage"]:
        money -= item["Mage"][item_to_buy]
    elif position_input == "ADC" and item_to_buy in item["ADC"]:
        money -= item["ADC"][item_to_buy]
    elif position_input == "Fighter" and item_to_buy in item["Fighter"]:
        money -= item["Fighter"][item_to_buy]
    elif position_input == "Jungle":
        if jungle_position == "AD" and item_to_buy in item["Jungle"]["AD"]:
            money -= item["Jungle"]["AD"][item_to_buy]
        elif jungle_position == "AP" and item_to_buy in item["Jungle"]["AP"]:
            money -= item["Jungle"]["AP"][item_to_buy]

if count_buy == 0:
    print("Perfect")
else:
    items_to_buy_str = " ".join([item for item in buy_item if item not in item[position_input]])
    print(f"{items_to_buy_str} {money} Gold")
