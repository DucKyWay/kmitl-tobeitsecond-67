ph_input = float(input())
if ph_input > 7 and ph_input <= 14:
    print("akaline")
elif ph_input == 7:
    print("neutral")
elif ph_input < 7 and ph_input >= 0:
    print("acidic")
else:
    print("error")