# Вводятся числа, пока не введут 0. Найти произведение чисел, оканчивающихся на 4.

# mult = 1
# number = int(input())
# while number != 0:
#     if number % 10 == 4:
#         mult *= number
#     number = int(input())
# if mult == 1:
#     mult = 0
# print(mult)


# Вводятся строки, пока не будет введена пустая строка. Если длина очередного введеного слова равна 5, то
# нужно вывести сообщение "YES" и прекратить возможность ввода для пользователя, если таких слов нет, то
# вывести 'NO' один раз в конце.

# some_str = input()
# while some_str:
#     if len(some_str) == 5:
#         print('YES')
#         break
#     some_str = input()
# else:
#     print('NO')


# i = 0
# while i <= 10:
#     print(i)
#     i += 1



# Переменная итератор используется внутри цикла.

# for i in 'hello':
#     print(i)

# for j in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
#     print(j ** 2)

# range()
# for number in range(1, 11):  # 1, 2, 3, 4...
#     print(number)
#
# for number in range(5):
#     print(number)
#
# for number in range(2, 101, 2):
#     print(number, end=' ')

# for number in range(10, 1, -2):
#     print(number)


# Переменная итератор не используется внутри цикла.
# 100 раз вывести слово hello в консоль

# i = 1
# while i <= 100:
#     print('Hello')
#     i += 1

# for _ in range(100):  # 0, 1, 2, 3, 4, 5, 6, 7, 8...99
#     print('Hello')

# Вводится количество чисел, затем сами числа, найти сумму чисел, кратных 3.
# n = int(input('Введите кол-во чисел: '))  # 10
# summa = 0
# for _ in range(n):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#     number = int(input())
#     if number % 3 == 0:
#         summa += number
# print(summa)


# Вводится количество чисел, затем сами числа, если число = 10, вывести YES и закончить ввод,
# в конце вывести NO если никакое из чисел не было равно 10.

# n = int(input('Введите кол-во чисел: '))
# for _ in range(n):
#     number = int(input())
#     if number == 10:
#         print('YES')
#         break
# else:
#     print('NO')

# a = int(input('Введите число: '))
# first = 0
# second = 1
# third = first + second
# count = 3
# while third < a:
#     first = second
#     second = third
#     third = first + second
#     count += 1
# if third == a:
#     print(count)
# else:
#     print(-1)

# num_day = int(input('Введите колличество дней: '))
#
# max_count = 0
# temp_count = 0
#
# for _ in range(num_day):
#     temperature = int(input('Введите температуру: '))
#     if temperature >= 0:
#         temp_count += 1
#     else:
#         temp_count = 0
#     if temp_count > max_count:
#         max_count = temp_count
# print(max_count)

watermelons = int(input('Введите кол-во арбузов: '))
# привет
max_kg = int(input('Введите массу арбуза: '))
min_kg = max_kg
for _ in range(watermelons - 1):
    weight = int(input('Введите массу арбуза: '))
    if weight > max_kg:
        max_kg = weight
    else:
        if weight < min_kg:
            min_kg = weight
print(f'Для себя любимого - {max_kg}, для любимой тещи - {min_kg}')