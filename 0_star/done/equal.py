'''Hello <i>Judge'''

def main():
    '''Main Function'''
    box_1 = int(input())
    box_2 = int(input())
    chk_box_1 = (box_1 > 0) * box_1
    chk_box_2 = (box_2 > 0) * box_2
    if chk_box_1 == chk_box_2:
        print("Equal")
    elif chk_box_1 != chk_box_2:
        print("Not Equal")

main()
