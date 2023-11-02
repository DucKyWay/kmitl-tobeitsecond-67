# OTP ที่มี 4 หลัก จะต้องมีเลขซ้ำกัน 1 ตัว, 2 หลัก (1120, 0850, 4543)
# OTP ที่มี 6 หลัก จะต้องมีเลขซ้ำกัน 2 ตัว, 4 หลัก หรือ 1 ตัว 3 หลัก (151567, 997882, 321324, 115167, 987666)
# OTP ที่มี 8 หลัก จะต้องมีเลขซ้ำกัน 3 ตัว, 6 หลัก หรือ 2 ตัว 6 หลัก (11223345, 68682400, 84886044)

from collections import Counter

def check_otp(otp):
    count = Counter(otp)
    values = list(count.values())
    
    if len(otp) == 4 and 2 in values:
        return True
    elif len(otp) == 6 and (values.count(4) == 1 or values.count(3) == 1):
        return True
    elif len(otp) == 8 and (values.count(6) >= 1 or values.count(3) >= 1):
        return True
    else:
        return False

while True:
    otp = input()
    if otp == '0':
        break
    if check_otp(otp):
        print("Valid")
    else:
        print("Invalid")