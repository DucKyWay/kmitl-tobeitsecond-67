sensitivity_check = 100.00
min_sen_chk, max_sen_chk = 0, float('inf')

while True:
    print(f'{sensitivity_check:.2f}?')
    sensitivity_feel = input()
    
    if sensitivity_feel == 'F':
        max_sen_chk = min(max_sen_chk, sensitivity_check)
    elif sensitivity_feel == 'S':
        min_sen_chk = max(min_sen_chk, sensitivity_check)
    elif sensitivity_feel == 'D':
        break
    
    if max_sen_chk == float('inf'):
        sensitivity_check *= 2
    else:
        sensitivity_check = (min_sen_chk + max_sen_chk) / 2

print(f'Your sensitivity is {sensitivity_check:.2f}.')
