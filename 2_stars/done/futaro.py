def main():
    ichika, nino, miku, yotsuba, itsuki, teach, day = int(input()), int(input()), int(input()), int(input()), int(input()), float(input()), int(input())

    ichika_result = "Pass" if (teach * ichika/100 * day) > 60 else "Fail"
    nino_result = "Pass" if (teach * nino/100 * day) > 60 else "Fail"
    miku_result = "Pass" if (teach * miku/100 * day) > 60 else "Fail"
    yotsuba_result = "Pass" if (teach * yotsuba/100 * day) > 60 else "Fail"
    itsuki_result = "Pass" if (teach * itsuki/100 * day) > 60 else "Fail"

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
