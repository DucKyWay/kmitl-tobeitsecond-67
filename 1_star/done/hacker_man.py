# a, f, k, p, u, z : 1 ชั้น
# b, g, l, q, v : 2 ชั้น
# c, h, m, r, w : 3 ชั้น
# d, i, n, s, x : 4 ชั้น
# e, j, o, t, y : 5 ชั้น
# เราจะกรอกรหัส 5 ตัวน้องๆต้องตรวจว่าเจาะสำเร็จหรือไม่
# ถ้าสำเร็จตอบ"Unlock" ถ้าไม่บอกพี่หน่อยว่าเหลือกี่ชั้น

hack_key = {
    "a": 2,      "f": 2,    "k": 2,     "p": 2,     "u": 2,     "z": 2, 
    "b": 4,      "g": 4,    "l": 4,     "q": 4,     "v": 4,
    "c": 6,      "h": 6,    "m": 6,     "r": 6,     "w": 6,
    "d": 8,      "i": 8,    "n": 8,     "s": 8,     "x": 8,
    "e": 10,     "j": 10,   "o": 10,    "t": 10,    "y": 10
}
unlock = 0
for i in range(5) :
    code = input()
    unlock += hack_key[code]
if unlock >= 25:
    print("Unlock")
else:
    print(25 - unlock)