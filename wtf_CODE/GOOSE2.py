import json

duck_list = []
innocent_list = []
dead = []

input_line = input()
while input_line != "End":
    try:
        data = json.loads(input_line)
        name, role = next(iter(data.items()))
        
        if role == "Duck":
            duck_list.append(name)
        elif role == "Innocent":
            innocent_list.append(name)
    except json.JSONDecodeError:
        if input_line not in ["Start", "End"]:
            dead.append(input_line)

    input_line = input()

remaining_ducks = len(duck_list)
print(remaining_ducks, "Ducks Remain")
print("***Alive***")
for name in duck_list + innocent_list:
    print(f"{name} : Innocent" if name in innocent_list else f"{name} : Duck")

print("***Dead***")
for name in dead:
    print(f"{name} : Dead")
