# проверка на полиндром

def check_palindrome(array):
    flag = True
    for index in range(1,len(array) // 2):
        if array[index - 1] != array[-index]:
            flag = False
    return flag


lst = list(input("Введите данные для проверки на полиндром: "))
print(check_palindrome(lst))

#################
def rec_palindrome(array):
    if len(array) == 0:
        return True
    elif array[0] == array[-1]:
        return rec_palindrome(array[1:-1])
    return False
print(rec_palindrome(lst))

#################
def reverse(array, counter = 0):
    if counter == len(array)-1:
        return array[counter]
    return reverse(array, counter + 1) + array[counter]

lst_2 = list(reverse(lst))
if lst == lst_2:
    print(True)
else:
    print(False)
    