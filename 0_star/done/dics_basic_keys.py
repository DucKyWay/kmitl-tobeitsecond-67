university_dict = {
    "MU" : "Mahidol University",
    "CU" : "Chulalongkorn University",
    "CMU" : "Chiang Mai University",
    "KU" : "Kasetsart University",
    "PSU" : "Prince of Songkla University",
    "KKU" : "Khon Kaen University",
    "TU" : "Thammasat University",
    "KMUTT" : "King Mongkut's University of Technology Thonburi",
    "RU" : "Ramkhamhaeng University",
    "KMITL" : "King Mongkut's Institute of Technology Ladkrabang",
}
university = str(input())
if university in university_dict:
    print(university_dict[university])
else:
    print("Error")