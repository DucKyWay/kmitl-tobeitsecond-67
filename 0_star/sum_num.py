def main():

    total = 0
    while True:
        num = int(input())
        if num == -1:
            break
        total += num

    print(total)
main()