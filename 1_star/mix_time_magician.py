# เดือนกุมภาพันธ์ มี 14 วัน
# งานของน้อง คือ ให้เขียนโปรแกรมที่ช่วยบอกให้พี่ทราบว่า วันที่ x เดือน y นั้นคือวันอะไร
# เช่น วันที่ 5 เดือน 3 ก็คือ วันที่ 3 มีนาคม วันที่ 11 เดือน 11 ก็คือ วันที่ 11 พฤศจิกายน
# โดยที่น้องทราบมาเพียงว่าวันที่ 5 มกราคม คือ วันจันทร์
# หากวันหรือเดือนที่รับเข้ามาไม่อยู่ในเงื่อนไขข้างต้น ตัวอย่างเช่น วันที่ 32 เดือน 1
# ให้ตอบว่า Invalid Time

def calculate_day_of_week(day, month):
    days_in_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_in_month = [31, 14, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12 or day < 1 or day > days_in_month[month - 1]:
        return "Invalid Time"

    total_days = day
    for i in range(month - 1):
        total_days += days_in_month[i]

    day_of_week_index = total_days % 7
    day_of_week = days_in_week[day_of_week_index]
    return day_of_week

def main():
    day, month = int(input()), int(input())
    result = calculate_day_of_week(day, month)
    print(result)
main()
