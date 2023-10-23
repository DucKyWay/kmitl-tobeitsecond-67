def check_result(score, teach, day):
    score_l = score / 100 * day
    can_pass = teach / 100 * day
    return "Pass" if score_l + can_pass >= 0.6 * can_pass else "Fail"
    
def main():
    ichika, nino, miku, yotsuba, itsuki, teach, day = int(input()), int(input()), int(input()), int(input()), int(input()), float(input()), int(input())

    ichika_result = check_result(ichika, teach, day)
    nino_result = check_result(nino, teach, day)
    miku_result = check_result(miku, teach, day)
    yotsuba_result = check_result(yotsuba, teach, day)
    itsuki_result = check_result(itsuki, teach, day)

    chk_pass = 0
    if ichika_result == "Pass":
        chk_pass += 1
    if nino_result == "Pass":
        chk_pass += 1
    if miku_result == "Pass":
        chk_pass += 1
    if yotsuba_result == "Pass":
        chk_pass += 1
    if itsuki_result == "Pass":
        chk_pass += 1

    print("Ichika :", ichika_result)
    print("Nino :", nino_result)
    print("Miku :", miku_result)
    print("Yotsuba :", yotsuba_result)
    print("Itsuki :", itsuki_result)

    if chk_pass < 3:
        print("Futaro Outtt!!!")
main()
