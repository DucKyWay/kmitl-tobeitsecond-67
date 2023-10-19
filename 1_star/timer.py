# อย่าลืมเติมหน่วยของ วัน เวลา นาที วินาที ด้วยล่ะ ถ้ามันมากกว่า 1 ก็อย่าลืมเติม s ด้วย

# ห้ามใช้ if else!!!
# Input Specification
# 1 บรรทัด จำนวนเต็มบวกหรือศูนย์ เป็นจำนวนวินาที

# Output Specification
# 1 บรรทัด เป็นประโยคบอกวัน ชั่วโมง นาที วินาที มีจุดต่อท้ายประโยค
# 1 day 6 hours 50 minutes 1 second.

'''Hello <i>Judge'''

def main():
    '''Main Function'''
    time = int(input())
    balance = time
    day_left, hour_left, min_left, sec_left= 0, 0, 0, 0

    day_left = (balance >= 84000) * balance // 84000 and balance // day_left

    print(day_left)

main()

# if balance >= 84000: #day
#     day_left = balance // 84000
#     balance //= day_left
# else:
#     dayleft = 0

# if balance >= 3600: #hour
#     hour_left = balance // 3600
#     balance //= hour_left
# else:
#     hour_left = 0

# if balance >= 60: #min
#     min_left = balance // 60
#     balance //= min_left
# else:
#     min_left = 0

# if balance < 60: #sec
#     if balance != 0:
#         sec_left = balance
#     if balance == 0:
#         sec_left = 0 
# else:
#     sec_left = 0

# print(int(day_left))
# print(int(hour_left))
# print(int(min_left))
# print(int(sec_left))