from traceback import print_last

first,second,third = input("Введите три целых числа через пробел:").split()

if first == second and second == third and first == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print("0")
