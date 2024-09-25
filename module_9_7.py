# -*- coding: utf-8 -*-

def is_prime(func):
    def wrapper(*args):
        result_now = func(*args)
        cond = False
        if result_now != 0 and result_now not in range(-3, 4):
            if result_now > 0:
                for count in range(2, result_now // 2 + 1):
                    if result_now % count == 0:
                        cond = True
            else:
                for count in range(result_now // 2, -1):
                    if result_now % count == 0:
                        cond = True
        if cond == True and result_now != 0:
            result_string = 'Составное'
        elif cond == False and result_now != 0:
            result_string = 'Простое'
        else:
            result_string = 'Это просто 0, ни простой, ни составной'
        print(result_string)
        return result_now

    return wrapper


@is_prime
def sum_three(first, second, third):
    result_add = first + second + third
    return result_add


result = sum_three(-1, -1, -1)
print(result)
