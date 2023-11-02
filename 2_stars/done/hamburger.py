# ร้าน Fastfood แห่งหนึ่งขาย Hamburger ราคา a บาท เมื่อซื้อครบ b ชิ้น จะได้ฟรี c ชิ้น อยากกิน d ชิ้น

def main():
    '''Main Function'''
    price = int(input()) # ราคา
    pro = int(input()) # เมื่อซื้อครบ
    free = int(input()) # ได้ฟรี
    want = int(input()) # อยากกิน
    set = want // (pro + free)
    check_pro = want % (pro + free)
    if check_pro <= pro:
        get = (set * (pro + free)) + check_pro
        pay = (set * pro * price) + (check_pro * price)
    else:
        get = (set * (pro + free)) + (pro + free)
        pay = pro * price * (set + 1)

    print(f'{get} ชิ้น') # จำนวน Hamburger ที่ได้รับ
    print(f'{pay} บาท') # จำนวนเงินน้อยที่สุดที่เราต้องจ่าย
main()