hp_dedee = float(input()) # บรรทัด 1 เลือดของดีดี้(float)
adapt_dedee = float(input()) # บรรทัด 2 ค่าการปรับตัวที่ต้องครบ(float)
count_attack_paloy = int(input()) # บรรทัด 3 จำนวนการโจมตีของพาลอย(int)
adjustment = 0
dedee_skill = 0.3

for i in range(count_attack_paloy):
    damage_paloy = float(input()) # บรรทัด n+1 แดมเมจที่พาลอยโจมทีในแต่ละที (float)
    hp_dedee -= damage_paloy
    adjustment += (damage_paloy * adapt_dedee)

if hp_dedee <= 0: # ดีดี้ HP หมด
    print("ดีดี้โดนัท")
elif hp_dedee > 0 and adjustment >= adapt_dedee: # HP ดีดี้เหลือและค่าปรับตัวมากกว่าหรือเท่ากับที่กำหนด
    print("พาลอยซาชิมิ")
elif hp_dedee > 0 and adjustment <= adapt_dedee: # เมื่อดีดี้พลังชีวิตเหลือและค่าปรับตัวน้อยกว่าที่กำหนด
    print("ตายคู่")

# อันนี้พี่ว่าพลังพาลอยมันมากไปหน่อยนะใบ้ให้


# ดีดี้จะรับการโจมตีและนำไปเป็นค่าการปรับตัว โดยเมื่อดีดี้ได้รับการโจมตีจะนำความเสียหายที่ได้รับจำนวน 0.03 เท่าของค่าแดมเมจที่ได้รับ
# นำไปเป็นค่าการปรับตัว กล่าวคือเมื่อค่าปรับตัวครบ n หน่วย ดีดี้จะสามารถโจมตีพาลอยได้
# โดยถ้าดีดี้ยังมีพลังชีวิตเหลือจะสามารถโจมตีพาลอยได้(พาลอยจะซาชิมิทันที) แต่ถ้าดีดี้ Hp หมด ดีดี้จะกลายเป็นโดนัท 
# โดยพาลอยจะต้องโจมตีจนครบทุกครั้งก่อนดีดี้จึงจะมีโอกาสโจมตีสวน(ถ้าดีดี้ยังไม่โดนัทละก็นะ)

# ถ้าดีดี้ HP หมด = ดีดี้โดนัท ถ้า HP ดีดี้เหลือและค่าปรับตัวมากกว่าหรือเท่าที่กำหนด = พาลอยซาชิมิ เมื่อดีดี้พลังชีวิตเหลือและค่าปรับตัวน้อยกว่าที่กำหนด = ตายคู่

# didyHealth = float(input())
# didyTotalDM = 0
# # เมื่อดีดี้โดนโจมตีจนถึงในจุดที่กำหนดดีดี้จะสามารถโจมตีใส่ผู้ที่โจมตีดีดี้ได้แบบ 100%
# didyReUseDM = 0.03
# didyMaxReUseTotalDM = float(input())
# # บรรทัด 1 เลือดของดีดี้(float)
# # บรรทัด 2 ค่าการปรับตัวที่ต้องครบ(float)
# # บรรทัด 3 จำนวนการโจมตีของพาลอย(int)
# # บรรทัด n+1 แดมเมจที่พาลอยโจมทีในแต่ละที (float)
# praployTotalDM = int(input())
# for i in range(praployTotalDM) :
#     plaployDM = float(input())
#     didyTotalDM += plaployDM * didyReUseDM
#     didyHealth -= plaployDM

# if (didyHealth <= 0 ) :
#     print("ดีดี้โดนัท") 
# elif (didyHealth > 0 and didyTotalDM >= didyMaxReUseTotalDM) :
#     print("พาลอยซาชิมิ")
# elif (didyHealth > 0 and didyTotalDM <= didyMaxReUseTotalDM) :
#     print("ตายคู่")