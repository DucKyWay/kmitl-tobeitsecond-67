bullet = int(input())
enemy_hp = float(input())
gun_damage = float(input()) 
hp_remain = enemy_hp

for i in range(bullet):
    hp_remain -= gun_damage
    print(i+1, bullet-(i+1))
    if hp_remain <= 0:
        result = "dead : " + str(bullet - (i + 1)) + " bullet remain"
        break
else:
    result = "alive : " + str(hp_remain) + " health"
print(result)