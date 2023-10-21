def main():
    start = int(input())
    finish = int(input())

    times = finish - start
    i = start

    for i in range(times):
        print(start)
        start += 1
        i += 1
    print(start)
    print("Yahoo!")

main()