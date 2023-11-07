# จากนั้นก็ให้หาเลขฐานสองของแต่ละ จำนวนที่รับเข้ามาบวกด้วยความถี่ของจำนวนนั้น
# เช่น INPUT คือ
# 2
# 2
# 2
# OUTPUT ก็คือ 101 ซึ่งเกิดจากการนำ 2 มาบวกกับความถี่ของ 2 ก็คือ 3 (เพราะว่ามี 2 อยู่ 3 ตัว) บวกกันได้ 5 จากนั้นจึงนำไปแปลงเป็นเลขฐาน 2

# Output Specification
# จำนวนบรรทัดขึ้นอยู่กับ Input ประกอบด้วย ตัวเลขจำนวนเต็มและเลขฐานสองตามเงื่อนไขของโจทย์ข้างต้น คั่นด้วย "-->" โดยให้เรียงจากเลขจำนวนเต็มที่น้อยที่สุด

# 2-->101

num_list = []
while True:
    num = int(input())
    if num.lower() != "end":
        check = False
        for i in num_list:
            if i[0] == num:
                i[1] += 1
                check = True
                break
        if not check:
            num_list.append([num, 1])
    else:
        break

    print(num)

for i in num_list :
    number = int(i[0]) + i[1]
    two_b = "{0:b}".format(num)
    print(f'{i[0]}-->{two_b}')