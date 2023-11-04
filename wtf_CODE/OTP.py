# OTP ที่มี 4 หลัก จะต้องมีเลขซ้ำกัน 1 ตัว, 2 หลัก (1120, 0850, 4543)
# OTP ที่มี 6 หลัก จะต้องมีเลขซ้ำกัน 2 ตัว, 4 หลัก หรือ 1 ตัว 3 หลัก (151567, 997882, 321324, 115167, 987666)
# OTP ที่มี 8 หลัก จะต้องมีเลขซ้ำกัน 3 ตัว, 6 หลัก หรือ 2 ตัว 6 หลัก (11223345, 68682400, 84886044)

# Input Specification
# OTP ที่มี 4, 6, หรือ 8 หลัก; เป็นตัวเลขทั้งหมด
# บรรทัดสุดท้ายคือเลข 0 เป็นตัวบอกว่าไม่มีค่ารับเข้าอีกแล้ว

# Output Specification
# Valid หาก OTP ถูกต้องตามเงื่อนไข ตามลำดับที่ได้รับเข้ามา
# Invalid หากไม่ถูกต้อง

while True:
    num_input = input()
    if num_input == '0':
        break
    num_list = list(num_input)
    if len(str(num_input)) == 4:
        if len(set(str(num_input))) < 4:
            print("Valid")
        else:
            print("Invalid")

    elif len(str(num_input)) == 6:
        is_valid = False
        for i in range(4, len(str(num_input))):
            if str(num_input)[i] == str(num_input)[i-4]:
                if str(num_input).count(str(num_input)[i]) == 2 or str(num_input).count(str(num_input)[i]) == 3:
                    is_valid = True
                    break
        if is_valid:
            print("Valid")
        else:
            print("Invalid")

    elif len(str(num_input)) == 8:
        print("============================")
    else:
        print("Invalid")