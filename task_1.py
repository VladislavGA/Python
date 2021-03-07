'''1. Реализовать вывод информации о промежутке времени в зависимости
 от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.'''

print('*' * 150)
print('Задание 1')
print('Введите кол-во секунд, которые необходимо конвертировать в')
seconds = int(input('секунды, минуты, часы и дни: '))
print(f'Вы ввели: {seconds} сек.')

minute = seconds // 60
hour = minute // 60
day = hour //24
month = day // 30
year = month // 12

rem_sec = seconds - (minute * 60)
rem_min = minute - (hour * 60)
rem_hour = hour - (day * 24)
rem_day = day - (month * 30)
rem_month = month - (year * 12)

print(f'{seconds} сек. = {minute} мин. {rem_sec} сек.')
print(f'{seconds} сек. = {hour} час. {rem_min} мин. {rem_sec} сек')
print(f'{seconds} сек. = {day} сут. {rem_hour} час. {rem_min} мин. {rem_sec} сек')
print(f'{seconds} сек. = {month} мес. {rem_day} сут. {rem_hour} час. {rem_min} мин. {rem_sec} сек')
print(f'{seconds} сек. = {year} год. {rem_month} мес. {rem_day} сут. {rem_hour} час. {rem_min} мин. {rem_sec} сек')

'''2.	Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
a.	Вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7. Например,
число «19 ^ 3 = 6859» будем включать в сумму,
так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
b.	К каждому элементу списка добавить 17 и
заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.
c.	* Решить задачу под пунктом b, не создавая новый список.
'''
print('*' * 150)
print('Задание 2')
odd_numbers = []  #Создать список, состоящий из кубов нечётных чисел от 1 до 1000
for i in range(1, 1000):
    if i % 2 != 0:
        odd_numbers.append(i**3)
i = 0
amount_digits_7 = 0
for element in odd_numbers:
    amount_digits = 0
    while element > 0:  #перебираем каждый элемент из созданного списка и находим его сумму цифр
        digit = element % 10
        amount_digits = amount_digits + digit
        element = element // 10
    if amount_digits % 7 == 0:  #проверяем условие сумма цифр которых делится нацело на 7.
        amount_digits_7 += odd_numbers[i]  #Вычисляем сумму
    i += 1

print('Cписок, из кубов нечётных чисел: ', odd_numbers)

print('Сумма чисел: ', amount_digits_7)

i = 0
for element in odd_numbers:
    odd_numbers[i] = element + 17
    i += 1

print('Cписок, из кубов нечётных чисел +17: ', odd_numbers)

i = 0
amount_digits_17 = 0
for element in odd_numbers:
    amount_digits = 0
    while element > 0:
        digit = element % 10
        amount_digits = amount_digits + digit
        element = element // 10
    if amount_digits % 7 == 0:
        amount_digits_17 += odd_numbers[i]
    i += 1

print('Сумма чисел: ', amount_digits_17)

'''3.	Реализовать склонение слова «процент» для чисел до 20.
 Например, задаем число 5 — получаем «5 процентов»,
  задаем число 2 — получаем «2 процента».
 Вывести все склонения для проверки.'''

print('*' * 150)
print('Задание 3')

number = int(input('Введите число от 1 до 20: '))
percent = ['процент', 'процента', 'процентов']

if 1 < number < 5:
    print('У Вас: ', number, percent[1])
elif 4 < number < 21 or number == 0:
    print('У Вас: ', number, percent[2])
elif number == 1:
    print('У Вас: ', number, percent[0])
else:
    print('Вы ввели число не по условию! ')

print('*' * 25)
print('Проверка: ')

for n in range (0, 21):
    if 1 < n < 5:
        print(n, percent[1])
    elif 4 < n < 21 or n == 0:
        print(n, percent[2])
    else:
        print(n, percent[0])



