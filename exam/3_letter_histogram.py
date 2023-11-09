# ให้น้องสร้างแผนภูมิของ ความถี่ตัวอักษร ของข้อความที่ได้รับเข้ามา 1 บรรทัด
# โดยในข้อความอาจจะมีช่องว่าง, ตัวเลข, หรืออักขระพิเศษปะปนมาด้วย ให้นับเฉพาะตัวอักษรเท่านั้น
# โดยที่ เรียงจากอักษรพิมพ์ใหญ่ ไปพิมพ์เล็ก [ A-Z -> a-z ]
# รูปแบบแผนภูมิ
# ฝั่งซ้ายจะเป็นตัวเลขความถี่สามหลักต่อด้วยเครื่องหมาย | และช่องว่าง 1 ช่อง ถ้าตัวเลขไม่ถึงสามหลัก (เช่น 1, 2, 15, 26)
# ให้เติมศูนย์(0)ไว้ข้างหน้าให้ครบสามหลัก เช่น 001, 002, 015, 026 มั่นใจได้ว่าจะไม่มีตัวอักษรไหนมีความถี่เกิน 999 ใน Testcase
# โดยที่บรรทัดแรกจะต้องเป็นตัวเลขความถี่ของตัวอักษรที่มีความถี่สูงสุด
# บรรทัดต่อๆไปจะมีความถี่ลดลงมาเรื่อยๆ จนถึง 1
# บรรทัดสุดท้ายของแผนภูมิ จะต้องใส่เครื่องหมาย > 4 ตัว ตามด้วยช่องว่าง ก่อนขึ้นตัวอักษรแรก
# ในแต่ละตัวอักษรให้เว้นวรรคหนึ่งช่อง
# การแสดงความถี่ (^) ของแต่ละตัวอักษรมีช่องว่าง 1 ช่องคั่นอยู่เสมอ
# จากนั้นในบรรทัดสุดท้ายให้น้องแสดงค่า MAX, MIN, AVG(ค่าเฉลี่ย) และ S.D.(ส่วนเบี่ยงเบนมาตรฐาน) ของชุดข้อมูลความถี่ของตัวอักษรในประโยคที่รับเข้ามา
# โดยให้แสดงเป็นตัวเลขทศนิยม 2 ตำแหน่ง
# image1
# MAX คือ ค่าสูงสุดของชุดข้อมูล MIN คือ ค่าต่ำสุดของชุดข้อมูล
# AVG คือ ค่าเฉลี่ยของชุดข้อมูล S.D. คือ ส่วนเบี่ยงเบนมาตรฐานของชุดข้อมูล ซึ่งพี่มีสูตรให้
# image2

# Input Specification
# 1 บรรทัด เป็นประโยคหนึ่งประโยค
# ประกอบไปด้วยตัวอักษรภาษาอังกฤษตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่ ช่องว่าง หรือ อักขระพิเศษ
# มั่นใจได้ว่าจะเป็นประโยคที่มีความยาวมากกว่า 5 ตัวอักษร

# Output Specification
# กราฟตามภาพด้านบน
# จำนวนบรรทัด คือ ความถี่ตัวอักษรที่มากที่สุด + 2
# ในบรรทัดสุดท้าย การแสดงค่า MAX, MIN, AVG(ค่าเฉลี่ย) และ S.D.(ส่วนเบี่ยงเบนมาตรฐาน)
# ให้คั่นด้วยเครื่องหมายคอมม่า + ช่องว่าง 1 ช่อง
