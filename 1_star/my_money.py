'''Hello <i>Judge'''

def main():
    '''Main Function'''
    p_tide = int(input())
    p_tide_float = float(p_tide)
    price = (p_tide_float/3)/2
    total = (p_tide > 0) * ('%.2f' % ((p_tide_float/3) - (price*(75/100))))
    print(total, "Baht")
main()