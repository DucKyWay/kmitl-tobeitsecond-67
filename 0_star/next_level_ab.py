'''Hello <i>Judge'''

def main():
    '''Main Function'''
    a = int(input())
    b = int(input())
    chk_a = (a >= 0) * a or (a == 0) * str(a).zfill(2)
    chk_b = (b >= 0) * b or (b == 0) * str(b).zfill(2)
    val_1 = str(chk_a) + str(chk_b)
    val_2 = str(chk_b) + str(chk_a)
    print(val_1, "+", val_2, "=", int(val_1) + int(val_2))

main()

# จงเขียนโปรแกรมที่รับค่าเป็นตัวเลขจำนวนเต็มบวกหรือศูนย์ 2 ตัว
# จากนั้นหาผลบวกของการนำเลขจำนวนเต็มตัวแรกมาต่อกับตัวสอง และ ตัวสองมาต่อกับตัวแรก

# Input: 1
# Input: 2
# Output: 12 + 21 = 33