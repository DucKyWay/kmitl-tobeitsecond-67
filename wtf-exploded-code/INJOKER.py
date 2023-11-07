skillMarble = {
    "QQQ" : "COLD SNAP",
    "QQW" : "GHOST WALK",
    "QQE" : "ICE WALL",
    "WWW" : "E.M.P",
    "WWQ" : "TORNADO",
    "WWE" : "ALACRITY" ,
    "EEE" : "SUN STRIKE",
    "EEQ" : "FORGE SPIRIT",
    "EEW" : "CHAOS METEOR",
    "QWE" : "DEFEANING BLAST"
}
skillList = []
skillInput = input()

for i in skillInput :
    skillList.append(i)
    if i == 'RS' :
        skillList.pop()
        break
combolist = []

for i in range(len(skillList) - 2):
    skill_combo = skillList[i:i+3]
    combo_str = ''.join(skill_combo)
    if combo_str in skillMarble:
        combolist.append(skillMarble[combo_str])
combolist = sorted(combolist , reverse=True)

if combolist :
    for i in range(len(combolist)) :
        if i >= len(combolist) - 1 :
            print(combolist[i])
        else :
            print(combolist[i] , end=', ')
else :
    print("EZ MID")