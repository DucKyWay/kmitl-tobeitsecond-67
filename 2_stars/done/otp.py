# OTP ที่มี 4 หลัก จะต้องมีเลขซ้ำกัน 1 ตัว, 2 หลัก (1120, 0850, 4543)
# OTP ที่มี 6 หลัก จะต้องมีเลขซ้ำกัน 2 ตัว, 4 หลัก หรือ 1 ตัว 3 หลัก (151567, 997882, 321324, 115167, 987666)
# OTP ที่มี 8 หลัก จะต้องมีเลขซ้ำกัน 3 ตัว, 6 หลัก หรือ 2 ตัว 6 หลัก (11223345, 68682400, 84886044)

while True:
    num = input()
    if num == '0':
        break
    count_num = [num.count(str(i)) for i in range(10)]
    if len(num) == 4 and count_num.count(2) == 1:
        print("Valid")
    elif len(num) == 6 and (count_num.count(2) == 2 or count_num.count(3) == 1):
        print("Valid")
    elif len(num) == 8 and (count_num.count(2) == 3 or count_num.count(3) == 2):
        print("Valid")
    else:
        print("Invalid")