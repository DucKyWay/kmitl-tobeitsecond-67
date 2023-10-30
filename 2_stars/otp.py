# OTP ที่มี 4 หลัก จะต้องมีเลขซ้ำกัน 1 ตัว, 2 หลัก (1120, 0850, 4543)
# OTP ที่มี 6 หลัก จะต้องมีเลขซ้ำกัน 2 ตัว, 4 หลัก หรือ 1 ตัว 3 หลัก (151567, 997882, 321324, 115167, 987666)
# OTP ที่มี 8 หลัก จะต้องมีเลขซ้ำกัน 3 ตัว, 6 หลัก หรือ 2 ตัว 6 หลัก (11223345, 68682400, 84886044)

# Input Specification
# OTP ที่มี 4, 6, หรือ 8 หลัก; เป็นตัวเลขทั้งหมด
# บรรทัดสุดท้ายคือเลข 0 เป็นตัวบอกว่าไม่มีค่ารับเข้าอีกแล้ว

# Output Specification
# Valid หาก OTP ถูกต้องตามเงื่อนไข ตามลำดับที่ได้รับเข้ามา
# Invalid หากไม่ถูกต้อง

def main():
    while True:
        otp = int(input())
        otp_list = [int(i) for i in str(otp)]

        two_pillar = 0
        # print(otp_list.count(2))
        if otp == 0:
            break
        
        if len(str(otp)) == 4 or len(str(otp)) == 6 or len(str(otp)) == 8:
            for i in range(len(str(otp))):
                for j in range(10):
                    chk_otp = otp_list.count(j)
                    if chk_otp > 2:
                        two_pillar += 1
            if two_pillar <= 1:
                print("Valid")
            else:
                print("Invalid")
        two_pillar = 0
main()
