# เขากางแผนที่ออกมาเพื่อที่จะเช็คว่า มีบ่อน้ำพุที่จะช่วยฟื้นฟูมานาให้กลับมาเต็มได้ ณ จุดไหนของเส้นทางบ้าง
# ซึ่งเขาพบว่ามีบ่อน้ำพุตั้งอยู่เป็นระยะๆอยู่ n บ่อ
# แต่ละบ่อจะอยู่ห่างจาก จุดเริ่มต้น อยู่ k หน่วย
# ในขณะที่มานาเต็ม(r มานา) Invoker จะสามารถเดินทางได้ระยะ r หน่วย และจุดหมายอยู่ห่างจากจุดเริ่มต้นเป็นระยะทาง c หน่วย
# ทุกๆระยะทาง 1 หน่วย จะสูยเสีย 1 มานา
# แต่ Invoker นั้นไม่อยากแวะเติมมานาที่บ่อน้ำพุบ่อยๆ เพราะจะเป็นการเสียเวลา(พอดีเค้าใจร้อนอ่าา)
# จึงเลือกที่จะไปให้ได้ไกลที่สุด จึงค่อยแวะไปบ่อน้ำพุเพื่อเติมมานา
# พ่อมด Invoker จึงอยากให้น้องเขียนโปรแกรมหาจำนวนครั้งที่น้อยที่สุดที่จะแวะไปเติมมานาที่บ่อน้ำพุ

# Input Specification
# 3 + n บรรทัด
# 1.ระยะห่างระหว่างจุดเริ่มต้น กับ จุดหมาย จำนวนจริงปริมาณสเกลาร์
# 2.ระยะทางที่ Invoker สามารถเดินทางได้ในขณะที่มานาเต็ม จำนวนจริงปริมาณสเกลาร์
# 3.จำนวนบ่อน้ำพุทั้งหมดในเส้นทาง จำนวนนับ
# อีก n บรรทัด , ระยะห่างของบ่อน้ำพุ วัดจากระยะห่างระหว่างบ่อน้ำพุนั้นๆ กับจุดเริ่มต้น(0) , จำนวนจริงปริมาณสเกลาร์

# Output Specification
# 1 บรรทัด จำนวนครั้งที่แวะบ่อน้ำพุ, จำนวนนับ
# หรือ
# 1 บรรทัด ถ้าหาก Invoker ไม่สามารถไปถึงจุดหมายได้ไม่ว่ากรณีใดๆ(เช่นมานาหมด) ให้ตอบว่า Out of mana

distance = input()
mana_max_distance = input()
fountain = int(input())
for i in range(fountain): 
    fountain_start_distance = input()