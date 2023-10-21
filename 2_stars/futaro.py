def main():

    ichika, nino, miku, yotsuba, itsuki, teach, days = int(input()), int(input()), int(input()), int(input()), int(input()), float(input()), int(input())
    if ichika < teach and nino < teach and miku < teach and yotsuba < teach and itsuki < teach:

        ichika_l = ichika * days * 0.6
        nino_l = nino * days * 0.6
        miku_l = miku * days * 0.6
        yotsuba_l = yotsuba * days * 0.6
        itsuki_l = itsuki * days * 0.6
        can_pass = (teach * days) * 0.6
        
        if ichika_l >= can_pass:
            ichika_result = "Pass"
        else: 
            ichika_result = "Fail"

        if nino_l >= can_pass:
            nino_result = "Pass"
        else: 
            nino_result = "Fail"  
            
        if miku_l >= can_pass:
            miku_result = "Pass"
        else: 
            miku_result = "Fail"

        if yotsuba_l >= can_pass:
            yotsuba_result = "Pass"
        else: 
            yotsuba_result = "Fail"

        if itsuki_l >= can_pass:
            itsuki_result = "Pass"
        else: 
            itsuki_result = "Fail"  

        chk_pass = [ichika_result, nino_result, miku_result, yotsuba_result, itsuki_result].count("Pass")

        print("Ichika:", ichika_result)
        print("Nino:", nino_result)
        print("Miku:", miku_result)
        print("Yotsuba:", yotsuba_result)
        print("Itsuki:", itsuki_result)

        if chk_pass < 3:
            print("Futaro Outtt!!!")

main()
