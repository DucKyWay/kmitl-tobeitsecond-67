# Description

# ณ ที่แห่งหนึ่งมีกบุ่มห่านอาศัยอยู่เป็นจำนวนมากแต่ทว่าก็กลับมี เป็ด จำนวนหนึ่งแฝงตัวเข้ามาแล้วฆ่า ห่าน ทิ้ง!!!!
# กลุ่มห่านเลยต้องช่วยกันโหวตว่าตัวไหนกันแน่คือเป็ดที่ฆ่าเพื่อนของพวกเค้าไป!
# โดยให้บอกรายชื่อของตัวที่เหลือรอดและรายชื่อของตัวที่ตาย โดยรายชื่อที่ออกมาเรียงกันแล้ว
# ลองใช้ตัวนี้ในการดึงข้อมูลมาดูนะครับ

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

ducks = {}

for i in range(10):
    player = input()
    name = "Innocent" if player == "Innocent" else "Duck"
    ducks[name] = i

def is_alive(name):
    if name in ducks:
        return ducks[name] == 1
    else:
        return False

for name in ducks:
    if is_alive(name):
        print(f"{name} is alive")
    else:
        print(f"{name} is dead")