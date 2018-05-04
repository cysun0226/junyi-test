

def factor_num(num):
    result_num = 0
    for i in range(1, num+1):
        if ((i % 3 == 0 or i % 5 == 0) and (i % 15 != 0)):
            result_num = result_num
        else:
            result_num += 1
    return result_num




num = int(input('\nPlease input a number: '))
print('> result = ' + str(factor_num(num)))
