import json
is_start, players, dead, alive, duck_count = False, {}, {}, {}, 0

while True:
    player_input = input()
    if player_input == "Start":
        is_start = True
    elif player_input == "End":
        break
    else:
        if not is_start:
            players.update(json.loads(player_input))
        else:
            dead.update({player_input : players[player_input]})

for i, _ in players.items():
    if i not in dead:
        alive.update({i : players[i]})
for i in alive:
    if players[i] == "Duck":
        duck_count += 1

# printttt
print(f"{duck_count} Ducks Remains")
if len(alive) > 0:
    print("***Alive***")
    for i, j in sorted(alive.items(), key=lambda item: item[0]):
        print(f"{i} : {j}")
if len(dead) > 0:
    print("***Dead***")
    for i, j in sorted(dead.items(), key=lambda item: item[0]):
        print(f"{i} : {j}")