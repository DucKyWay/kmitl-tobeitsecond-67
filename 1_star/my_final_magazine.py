bullet = int(input()) # กระสุนที่ยิงออกไปทั้งหมด
enemy_hp = float(input()) # เลือดของศัตรู
gun_damage = float(input()) # ความเสียหายของกระสุน 1 นัด
total_damage, bullet_remain = 0, bullet

for i in range(bullet):
    bullet_remain -= 1
    total_damage += gun_damage
    hp_remain = enemy_hp - total_damage

    if total_damage >= enemy_hp:
        print(f"dead : {bullet_remain} bullet remain")
        break
    else:
        print(f"alive : {hp_remain} health")
        break