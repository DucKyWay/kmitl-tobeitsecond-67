'''Hello <i>Judge'''

def main():
    '''Main Function'''
    radius_explode = int(input())
    stand = int(input())

    space_explode = (22/7) * radius_explode * radius_explode
    safezone = space_explode * 2
    if stand > safezone:
        print("Safe")
    else:
        print("Not Safe")
main()
