bullet = int(input()) # กระสุนที่ยิงออกไปทั้งหมด
enemy_hp = float(input()) # เลือดของศัตรู
gun_damage = float(input()) # ความเสียหายของกระสุน 1 นัด
hp_remain = enemy_hp
bullet_remain = bullet

for i in range(bullet):
    if hp_remain <= 0:
        result = "dead : " + str(bullet_remain) + " bullet remain"
        break
    hp_remain -= gun_damage
    bullet_remain -= 1

else:
    if hp_remain <= 0:
        result = "dead : 0 bullet remain"
    else:
        result = "alive : " + str(hp_remain) + " health"

print(result)
