def count_frequency(word):
    frequency = {}
    for i in word:
        frequency[i] = frequency.get(i, 0) + 1
    return frequency

def create_tower(word):
    frequencies = count_frequency(word)
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: (-x[1], x[0].lower()))

    tower = []
    tower.append("_" * 9)
    layer = ""
    for i, j in sorted_frequencies:
        layer += f"|{i} <-> {j}|"
        layer += "\n"
    tower.append(layer.rstrip())
    tower.append("*" * 9)
    return tower

input_word = input()
tower = create_tower(input_word)
for layer in tower:
    print(layer)
