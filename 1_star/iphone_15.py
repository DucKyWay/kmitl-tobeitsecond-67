'''Hello <i>Judge'''

def main():
    '''Main Function'''
    model = str(input())
    storage = str(input())

    if model == "iPhone 15":
        if storage == "128 GB":
            print(32900)
        elif storage == "256 GB":
            print(36900)
        else:
            print("Not Sell")
    elif model == "iPhone 15 Plus":
        if storage == "128 GB":
            print(37900)
        elif storage == "256 GB":
            print(41900)
        else:
            print("Not Sell")
    elif model == "iPhone 15 Pro":
        if storage == "128 GB":
            print(41900)
        elif storage == "256 GB":
            print(45900)
        else:
            print("Not Sell")
    elif model == "iPhone 15 Pro Max":
        if storage == "256 GB":
            print(48900)
        else:
            print("Not Sell")
    else:
            print("Not Sell")

main()
