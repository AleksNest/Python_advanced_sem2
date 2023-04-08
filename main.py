# Задача 2
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

print("Задача 2 'Перевод из десятичной в систему исчисления с основанием от 2 до 16'")

number = int(input("введите целое число\n"))
base = int(input("введите основание системы счисления, в которую надо перевести число\n"))
num = abs(number)
number_new = ''

while num:
    if num % base == 10:
        num_char = 'A'
    elif num % base == 11:
        num_char = 'B'
    elif num % base == 12:
        num_char = 'C'
    elif num % base == 13:
        num_char = 'D'
    elif num % base == 14:
        num_char = 'E'
    elif num % base == 15:
        num_char = 'F'
    else:
        num_char = str(num % base)
    number_new = num_char + number_new
    num //= base

if number < 0:
    number_new = "-" + number_new
if number == 0:
    number_new = "0"

print(f'          Число {number} в {base}-ой системе счисления = {number_new}')
print(f'Проверка: число {number} в 16-ой системе счисления = {hex(number)}')



# Задача 3
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
import math

print("\nЗадача 3 'сложение и умножение дробей'")

str_1 = "-32/52"
str_2 = "60/40"

def shortenFraction(n: int, m: int):                    # метод сокращения дроби
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return str(n // k) + "/" + str(m // k)
        else:
            k -= 1
    return str(n) + "/" + str(m)

def sum_fractions(str_1, str_2):                        # метод сложения двух дробей
    num_1 = str_1.split("/")
    num_2 = str_2.split("/")
    lcm_fraction = math.lcm(int(num_1[1]), int(num_2[1]))   # НОЗ дроби
    numeratorFraction_1 = int(lcm_fraction / int(num_1[1]) * int(num_1[0]))
    numeratorFraction_2 = int(lcm_fraction / int(num_2[1]) * int(num_2[0]))
    return shortenFraction(numeratorFraction_1 + numeratorFraction_2, lcm_fraction)

def mult_fraction(str1, str2):                          # метод умножения двух дробей
    num_1 = str1.split("/")
    num_2 = str2.split("/")
    #return int(num_1[0]) * int(num_2[0]) / (int(num_1[1]) * int(num_2[1]))
    return shortenFraction(int(num_1[0]) * int(num_2[0]), int(num_1[1]) * int(num_2[1]))

def check_fraction(str1, str2, operation):              # метод проверки вычисления дробей на функции Fraction
    num_1 = str1.split("/")
    num_2 = str2.split("/")
    if operation == "*":
        return Fraction(int(num_1[0]), int(num_1[1])) * Fraction(int(num_2[0]), int(num_2[1]))
    elif operation == "+":
        return Fraction(int(num_1[0]), int(num_1[1])) + Fraction(int(num_2[0]), int(num_2[1]))
    elif operation == "-":
        return Fraction(int(num_1[0]), int(num_1[1])) - Fraction(int(num_2[0]), int(num_2[1]))
    else:
        return Fraction(int(num_1[0]), int(num_1[1])) / Fraction(int(num_2[0]), int(num_2[1]))



print("Расчет по программе:")
print(f'{str_1} * {str_2} = {mult_fraction(str_1, str_2)}')
print(f'{str_1} + {str_2} = {sum_fractions(str_1, str_2)}')

print("\nПроверка по Fraction:")
print(f'{str_1} * {str_2} = {check_fraction(str_1, str_2, "*")}')
print(f'{str_1} + {str_2} = {check_fraction(str_1, str_2, "+")}')


