# 1.พนักงานคนใดที่ทำงานมากกว่าหรือเท่ากับ 10 เดือน ก็ถือว่าทำงานมาครบ 1 ปี เลย
# 2.จะต้องไม่มีพนักงานคนใดได้ Bonus เกิน 20 เท่าของเงินเดือน แม้จะทำงานมาเกิน 20 ปีก็ตาม
# 3.จะไม่มีพนักงานคนใดได้ Bonus น้อยกว่า 5000 บาท หรือ มากกว่า 1000000 บาท

salary, year, month = int(input()), int(input()), int(input())
if month >= 10 and month <= 12: month = 12

year_month = month // 12
year += year_month
bonus = salary * year

if bonus > (20 * salary):   bonus = 20 * salary
if bonus < 5000:            bonus = 5000
if bonus > 1000000:         bonus = 1000000
print(bonus)