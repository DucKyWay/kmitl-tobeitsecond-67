bullet = int(input()) # กระสุนที่ยิงออกไปทั้งหมด
enemy_hp = float(input()) # เลือดของศัตรู
gun_damage = float(input()) # ความเสียหายของกระสุน 1 นัด
hp_remain = enemy_hp

for _ in range(bullet):
    hp_remain -= gun_damage
    if hp_remain <= 0:
        result = "dead : " + str(bullet - _ - 1) + " bullet remain"
        # result = "dead : " + str(bullet - (_ + 1)) + " bullet remain"
        break
else:
    result = "alive : " + str(hp_remain) + " health"

print(result)
