# Description
# พี่อยากให้น้องๆสร้างกล่องที่มีความกว้าง X ความยาว Y
# จากนั้นก็ให้น้องลองหยิบดาว (*) จำนวน n ดวงลงไปใส่ในกล่อง เพื่อดูว่าพี่จะสามารถใส่ดาวลงไปได้ครบหรือเปล่า
# น้องต้องใส่ดาวลงไปในคอลัมน์ฝั่งซ้ายไล่ไปทางฝั่งขวาและต้องใส่ให้เต็มทั้งคอลัมน์ก่อน
# โดยพี่ขอบอกเลยว่าดาวแต่ละดวงจะตกลงไปยังใต้กล่องตามแรงโน้มถ่วงอันมหาศาล

# Input Specification
# 3 บรรทัด
# ค่า X โดยที่ X เป็นจำนวนเต็มมีค่ามากกว่า 0
# ค่า Y โดยที่ Y เป็นจำนวนเต็มมีค่ามากกว่า 0
# ค่า n เป็นจำนวนเต็มมากกว่าหรือเท่ากับ 0

# Output Specification
# กล่องที่ใส่ดาวแล้วตามเงื่อนไขของโจทย์ และอีก 1 บรรทัด คือประโยคที่บอกว่ามีดาวเหลืออยู่กี่ดวง
# ดูตัวอย่างจาก Sample output ได้

# 4
# 4
# 17

# ------
# |****|
# |****|
# |****|
# |****|
# ------
# There are 1 star left.

width, height, star, star_box = int(input()), int(input()), int(input), []
star_box.append("-" * (width + 2))

star_row = star % width

star_box.append("-" * (width + 2))
for i in star_box:
    print(i)