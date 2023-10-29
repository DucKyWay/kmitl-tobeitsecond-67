num_dict = {
    "0" : "rei",
    "1" : "ichi",
    "2" : "ni",
    "3" : "san",
    "4" : "shi",
    "5" : "go",
    "6" : "roku",
    "7" : "shichi",
    "8" : "hachi",
    "9" : "kyu",
    "10" : "ju",
    "100" : "hyaku",
}
num = str(input())
if num in num_dict:
    print(num_dict[num])
else:
    print("Error")