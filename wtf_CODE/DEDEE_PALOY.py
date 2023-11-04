hp_dedee = float(input()) # บรรทัด 1 เลือดของดีดี้(float)
adapt_dedee = float(input()) # บรรทัด 2 ค่าการปรับตัวที่ต้องครบ(float)
count_attack_paloy = int(input()) # บรรทัด 3 จำนวนการโจมตีของพาลอย(int)
adjustment = 0
dedee_skill = 0.3

for i in range(count_attack_paloy):
    damage_paloy = float(input()) # บรรทัด n+1 แดมเมจที่พาลอยโจมทีในแต่ละที (float)
    adjustment += damage_paloy * dedee_skill # คำนวณค่าปรับตัว
    hp_dedee -= damage_paloy

if hp_dedee <= 0: # ดีดี้ HP หมด
    print("ดีดี้โดนัท")
elif hp_dedee > 0 and adjustment >= adapt_dedee: # HP ดีดี้เหลือและค่าปรับตัวมากกว่าหรือเท่ากับที่กำหนด
    print("พาลอยซาชิมิ")
elif hp_dedee > 0 and adjustment <= adapt_dedee: # เมื่อดีดี้พลังชีวิตเหลือและค่าปรับตัวน้อยกว่าที่กำหนด
    print("ตายคู่")

# if hp_dedee <= 0: # ดีดี้ HP หมด
#     print("ดีดี้โดนัท")
# elif adjustment >= adapt_dedee:  # HP ดีดี้เหลือและค่าปรับตัวมากกว่าหรือเท่ากับที่กำหนด
#     print("พาลอยซาชิมิ")
# elif hp_dedee > 0 and adjustment < adapt_dedee:  # เมื่อดีดี้พลังชีวิตเหลือและค่าปรับตัวน้อยกว่าที่กำหนด
#     print("ตายคู่")