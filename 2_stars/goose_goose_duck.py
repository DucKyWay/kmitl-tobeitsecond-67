# Description

# ณ ที่แห่งหนึ่งมีกบุ่มห่านอาศัยอยู่เป็นจำนวนมากแต่ทว่าก็กลับมี เป็ด จำนวนหนึ่งแฝงตัวเข้ามาแล้วฆ่า ห่าน ทิ้ง!!!!
# กลุ่มห่านเลยต้องช่วยกันโหวตว่าตัวไหนกันแน่คือเป็ดที่ฆ่าเพื่อนของพวกเค้าไป!
# โดยให้บอกรายชื่อของตัวที่เหลือรอดและรายชื่อของตัวที่ตาย โดยรายชื่อที่ออกมาเรียงกันแล้ว
# ลองใช้ตัวนี้ในการดึงข้อมูลมาดูนะครับ

# ลองใช้พวก Dict/Dict method มาช่วยในการทำข้อนี้นะครับ
# https://www.w3schools.com/python/python_dictionaries.asp

# Input Specification
# หลายบรรทัด
# ใส่เป็นชื่อระหว่าง Innocent หรือ Duck เข้ามาเรื่อย ๆ จนกว่าจะเจอคำว่า Start
# จากนั้นให้ใส่รายชื่อของพวกที่ถูกฆ่าตายออกไปจนกว่าจะเจอคำว่า End

# Output Specification
# หลายบรรทัด
# บรรทัดแรก จำนวน Duck ที่เหลืออยู่
# บรรทัดที่สอง Alive
# บรรทัดที่สาม จนถึง N เป็นรายชื่อของผู้รอดชีวิตทั้งหมดตามด้วยบทบาท Innocent หรือ Duck
# บรรทัดต่อมา Dead
# บรรทัดต่อมา จนถึง N เป็นรายชื่อของผู้ตายทั้งหมดตามด้วยบทบาท Innocent หรือ Duck

# {"Smith" : "Innocent"}        1 Ducks Remains
# {"Jerry" : "Innocent"}        ***Alive***
# {"Pig" : "Innocent"}          Jerry : Innocent
# {"Tom" : "Innocent"}          Leo : Duck
# {"Leo" : "Duck"}              Tom : Innocent
# {"Amu" : "Duck"}              Yamato : Innocent
# {"Yamato" : "Innocent"}       ***Dead***
# {"Tusk" : "Innocent"}         Amu : Duck
# Start                         Pig : Innocent
# Smith                         Smith : Innocent    
# Pig                           Tusk : Innocent
# Amu   
# Tusk
# End

import json

duck_list = []
innocent_list = []
dead = []

while True:
    line = input()
    if line == "Start":
        if line != "End":
            dead.append(line)
        else:
            break
    
    data = json.loads(line)
    name, role = list(data.keys())[0], list(data.values())[0]
    
    if role == "Duck":
        duck_list.append(name)
    elif role == "Innocent":
        innocent_list.append(name)

remaining_ducks = len(duck_list)

print(remaining_ducks, " Ducks Remains")
print("***Alive***")
for name in duck_list + innocent_list:
    print(f"{name} : Innocent" if name in innocent_list else f"{name} : Duck")

print("***Dead***")
for name in innocent_list + duck_list:
    print(f"{name} : Innocent" if name in innocent_list else f"{name} : Duck")
