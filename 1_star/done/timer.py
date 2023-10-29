def main():
    time = int(input())
    balance = time
    day_left, hour_left, min_left, sec_left= 0, 0, 0, 0

    day_left = balance // 86400
    balance %= 86400

    hour_left = balance // 3600
    balance %= 3600

    min_left = balance // 60
    balance %= 60

    sec_left = balance

    day_left_chk = str(day_left) + " day"
    day_left_hour = day_left_chk + (day_left > 1) * "s"

    hour_left_chk = str(hour_left) + " hour"
    hour_left_hour = hour_left_chk + (hour_left > 1) * "s"

    min_left_chk = str(min_left) + " minute"
    min_left_hour = min_left_chk + (min_left > 1) * "s"

    sec_left_chk = str(sec_left) + " second"
    sec_left_hour = sec_left_chk + (sec_left > 1) * "s"

    print(day_left_hour, hour_left_hour, min_left_hour, sec_left_hour + ".")
main()