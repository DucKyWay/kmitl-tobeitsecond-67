'''Hello <i>Judge'''

def main():
    '''Main Function'''
    score = float(input())
    scores = (score >= 0) * (score <= 100) * round(score, 2)
    if scores >= 80:
        print("A")
    elif scores < 80 and scores >= 75:
        print("B+")
    elif scores < 75 and scores >= 70:
        print("B")
    elif scores < 70 and scores >= 65:
        print("C+")
    elif scores < 65 and scores >= 60:
        print("C")
    elif scores < 60 and scores >= 55:
        print("D+")
    elif scores < 55 and scores >= 50:
        print("D")
    else:
        print("F")
main()
