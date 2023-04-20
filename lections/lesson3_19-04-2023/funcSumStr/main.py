def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res


print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'f'))
# print(sum_str(1, 8, 9))
