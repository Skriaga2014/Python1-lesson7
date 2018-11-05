'''
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
'''

def txt(listo):
    #[7, 15, 0, 0, 0, 0, 63, 79, 81]
    #[1, 11, 0, 39, 42, 55, 0, 0, 0]
    #[2, 17, 26, 38, 0, 0, 0, 0, 90]
    #==========================


    txt = ''
    for i in listo:
        txt += '\n'
        for j in listo[listo.index(i)]:
            if j == 0:
                txt += '\t'
            else:
                txt += f'\t{j}'
    txt += '\n=========================================='
    return txt

def new_card():

    def rand(start, end, n):
        import random
        listo = []
        for i in range(n):
            a = random.randint(start, end)
            while a in listo:
                a = random.randint(start, end)
            listo.append(a)
        return listo

    from random import randint as random

    LINES = 3
    COLS = 9
    NUMS = 9

    card_list = []
    for i in range(LINES):
        card_list.append([])
        for j in range(COLS):
            card_list[i].append(random(1,NUMS) + 10 * j)

    #print(f'{card_list[0]}\n{card_list[1]}\n{card_list[2]}')

    error = 1
    while error == 1:
        error = 0
        iskl = [rand(0,8,4),rand(0,8,4),rand(0,8,4)]
        #print(iskl)
        for i in range(4):
            if iskl[0][i] in iskl[1] and iskl[0][i] in iskl[2]:
                error = 1

    for i in range(LINES):
        for j in iskl[i]:
            card_list[i][j] = 0

    #print(f'{card_list[0]}\n{card_list[1]}\n{card_list[2]}')

    error = 1
    while error != 0:
        for i in range(COLS):
            error = 0
            if card_list[0][i] > 0 and card_list[0][i] == card_list[1][i]:
                error = 1
                if card_list[1][i] != 9 + 10*i:
                    card_list[1][i] += 1
                else:
                    card_list[1][i] -= 1
            elif card_list[1][i] > 0 and card_list[1][i] == card_list[2][i]:
                error = 1
                if card_list[2][i] != 9 + 10 * i:
                    card_list[2][i] += 1
                else:
                    card_list[2][i] -= 1
            elif card_list[2][i] > 0 and card_list[2][i] == card_list[0][i]:
                error = 1
                if card_list[0][i] != 9 + 10 * i:
                    card_list[0][i] += 1
                else:
                    card_list[0][i] -= 1

    for i in range(LINES):
        if card_list[i][8] == 89 and random(1,3) == 2:
            card_list[i][8] = 90

    # print(f'\n{card_list[0]}\n{card_list[1]}\n{card_list[2]}')
    return card_list

def zacherk():
    global number
    global my_card
    global comp_card
    for line in my_card:
        if number in line:
            line[line.index(number)] = '-'
    for line in comp_card:
        if number in line:
            line[line.index(number)] = '-'

def win():
    global my_card
    global comp_card
    my_nums = 0
    for line in my_card:
        for n in line:
            if type(n) is int and n != 0:
                my_nums += 1
    comp_nums = 0
    for line in comp_card:
        for n in line:
            if type(n) is int and n != 0:
                comp_nums += 1

    if my_nums == 0 and comp_nums == 0:
        return [3]
    if my_nums == 0:
        return [1, 15 - comp_nums]
    if comp_nums == 0:
        return [2, 15 - my_nums]
    else:
        return [0, my_nums, comp_nums]

import random

my_card = new_card()
comp_card = new_card()
print('\n============= Ваша карточка ==============',txt(my_card))
print('\n========== Карточка компьютера ===========',txt(comp_card))
ret = [0]
num_num = 0
past_nums = []

while ret[0] == 0:
    #print(sorted(past_nums))


    number = random.randint(1, 90)
    while number in past_nums:
        number = random.randint(1, 90)

    past_nums.append(number)


    num_num += 1
    print(f'Ход {num_num}\nВыпал боченок под номером ------ {number} ------ \n(осталось {90 - num_num})')

    wrong = 0
    do = 0
    while do != 'y' and do != 'n':
        do = input('Зачеркнуть (y) или продолжить (n): ')

    if do == 'y':
        for line in my_card:
            if number not in line:
                wrong += 1
                if wrong == 2:
                    wrong = 0
        if wrong != 0:
            print('\nЗачеркивать нечего. Вы проиграли!')
            quit()
    elif do == 'n':
        for line in my_card:
            if number in line:
                wrong = 1
        if wrong != 0:
            print('\nВы пропустили число в карточке. Вы проиграли!')
            quit()

    zacherk()

    print('\n============= Ваша карточка ==============', txt(my_card))
    print('\n========== Карточка компьютера ===========', txt(comp_card))

    ret = win()
    if ret[0] == 0:
        print(f'У вас осталось {ret[1]} чисел. У компьютера - {ret[2]}')
    elif ret[0] == 2:
        print(f'Вы проиграли =((((. У вас осталось {15 - ret[1]}')
        quit()
    elif ret[0] == 1:
        print(f'Вы ВЫИГРАЛИ!!! У компьютера осталось {15 - ret[1]}')
        quit()
    elif ret[0] == 3:
        print('ПОРАЗИТЕЛЬНО! НИЧЬЯ!!!')
        quit()