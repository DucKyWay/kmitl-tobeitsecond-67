num_list = []
while True:
    num = int(input())
    if num.lower() != "end":
        check = False
        for i in num_list:
            if i[0] == num:
                i[1] += 1
                check = True
                break
        if not check:
            num_list.append([num, 1])
    else:
        break

    print(num)

for i in num_list :
    number = int(i[0]) + i[1]
    two_b = "{0:b}".format(num)
    print(f'{i[0]}-->{two_b}')