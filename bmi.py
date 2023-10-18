'''Hello <i>Judge'''

def main():
    '''Main Function'''
    weight = float(input())
    height = float(input())
    height_m_square = (height/10) * (height/10)
    bmi = (weight > 0) * (height > 0) * ('%.2f' % (weight/height_m_square * 100))
    print(bmi)
main()