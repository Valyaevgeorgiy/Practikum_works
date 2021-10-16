import re
import math
stroka = input('''
 _______________________________ 
| Введите выражение             |
|                               |
|_______________________________|

''')
pa = re.compile('\w+')
num_words = pa.findall(stroka)
stroka1 = ' '.join(num_words)          # выделяем необходимую часть строки чисел и операции для преобразований
stroka = stroka1.lower()               # и преобразуем также строку в список слов с помощью регулярных выражений

operations = {
'плюс': '+',
'минус': '-',
'умножить на': '*',
'умножить': '*',
'возвести в степень': '**',
'возвести': '**',
'разделить на': '/',
'разделить': '/',
'остаток от деления': '%'
}
                              # составляем словари названия базовых операций, чисел, цифр
parts_number = {
'десятая': 0.1,
'десятых': 0.1,
'десятые': 0.1,
'сотых': 0.01,
'сотая': 0.01,
'сотые': 0.01,
'тысячная': 0.001,
'тысячных': 0.001,
'тысячные': 0.001
}
parts_number2 = {
'одиннадцать': 11,
'двенадцать': 12,
'тринадцать': 13,
'четырнадцать': 14,
'пятнадцать': 15,
'шестнадцать': 16,
'семнадцать': 17,
'восемнадцать': 18,
'девятнадцать': 19,
'десять': 10,
'сто': 100
}
nat_numbers = {
'одна тысяча': 1000,
'тысяча': 1000,
'две тысячи': 2000,
'три тысячи': 3000,
'четыре тысячи': 4000,
'пять тысяч': 5000,
'шесть тысяч': 6000,
'семь тысяч': 7000,
'восемь тысяч': 8000,
'девять тысяч': 9000,
'сто': 100,
'двести': 200,
'триста': 300,
'четыреста': 400,
'пятьсот': 500,
'шестьсот': 600,
'семьсот': 700,
'восемьсот': 800,
'девятьсот': 900,
'одиннадцать': 11,
'двенадцать': 12,
'тринадцать': 13,
'четырнадцать': 14,
'пятнадцать': 15,
'шестнадцать': 16,
'семнадцать': 17,
'восемнадцать': 18,
'девятнадцать': 19,
'десять': 10,
'двадцать': 20,
'тридцать': 30,
'сорок': 40,
'пятьдесят': 50,
'шестьдесят': 60,
'семьдесят': 70,
'восемьдесят': 80,
'девяносто': 90,
'ноль': 0,
'одна': 1,
'один': 1,
'две': 2,
'два': 2,
'три': 3,
'четыре': 4,
'пять': 5,
'шесть': 6,
'семь': 7,
'восемь': 8,
'девять': 9
}

russian_number_system = {
'одна тысяча': 1000,
'тысяча': 1000,
'две тысячи': 2000,
'три тысячи': 3000,
'четыре тысячи': 4000,
'пять тысяч': 5000,
'шесть тысяч': 6000,
'семь тысяч': 7000,
'восемь тысяч': 8000,
'девять тысяч': 9000,
'сто': 100,
'двести': 200,
'триста': 300,
'четыреста': 400,
'пятьсот': 500,
'шестьсот': 600,
'семьсот': 700,
'восемьсот': 800,
'девятьсот': 900,
'одиннадцать': 11,
'двенадцать': 12,
'тринадцать': 13,
'четырнадцать': 14,
'пятнадцать': 15,
'шестнадцать': 16,
'семнадцать': 17,
'восемнадцать': 18,
'девятнадцать': 19,
'десять': 10,
'двадцать': 20,
'тридцать': 30,
'сорок': 40,
'пятьдесят': 50,
'шестьдесят': 60,
'семьдесят': 70,
'восемьдесят': 80,
'девяносто': 90,
'ноль': 0,
'один': 1,
'одна': 1,
'два': 2,
'две': 2,
'три': 3,
'четыре': 4,
'пять': 5,
'шесть': 6,
'семь': 7,
'восемь': 8,
'девять': 9,
'десятая': 0.1,
'десятых': 0.1,
'десятые': 0.1,
'сотых': 0.01,
'сотая': 0.01,
'сотые': 0.01,
'тысячная': 0.001,
'тысячных': 0.001,
'тысячные': 0.001
}

decimal_words0 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
decimal_words1 = {
1: 'один',
2: 'два',
3: 'три',
4:'четыре',
5: 'пять',
6: 'шесть',
7: 'семь',
8: 'восемь',
9: 'девять'}

def number_formation(number_words):  # вводим функцию, преобразующую список строк в число
    numbers = []
    rty = False
    jk = 0
    for number_word in number_words:
        if number_word in russian_number_system:
            numbers.append(russian_number_system[number_word])  # вносим в список числа (цифры) из словаря
            jk = number_word
            if number_word in parts_number2:
                rty = True
        else:
            continue
    if (jk == 'десятых') or (jk == 'десятая') or (jk == 'десятые'):
        return numbers[-1] * numbers[-2]
    elif (jk == 'сотых') or (jk == 'сотая') or (jk == 'сотые'):
        if rty == False:
            if len(numbers) == 3:
                return numbers[-1] * (numbers[-2] + numbers[-3])
            elif len(numbers) == 2:
                return numbers[-1] * numbers[-2]
        else:
            return numbers[-1] * numbers[-2]
    elif (jk == 'тысячных') or (jk == 'тысячная') or (jk == 'тысячные'):
        if rty == False:
            if len(numbers) == 4:
                return numbers[-1] * (numbers[-2] + numbers[-3] + numbers[-4])
            elif len(numbers) == 3:
                return numbers[-1] * (numbers[-2] + numbers[-3])
            elif len(numbers) == 2:
                return numbers[-1] * numbers[-2]
        else:
            if 100 in numbers:
                return numbers[-1] * (numbers[-2] + numbers[-3])
            else:
                return numbers[-1] * numbers[-2]

    if (len(numbers) == 4) and (type(numbers[-1]) != float):
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif (len(numbers) == 3) and (type(numbers[-1]) != float):
        return numbers[0] * numbers[1] + numbers[2]
    elif (len(numbers) == 2) and (type(numbers[-1]) != float):
        if 100 in numbers:
            return numbers[0] * numbers[1]
        else:
            return numbers[0] + numbers[1]
    else:
        return numbers[0]


def number_part_desf(pasd):
    cam = ''
    pa1 = str(pasd)
    if len(pa1) == 3:
        for i, j in nat_numbers.items():
            if j == int(pa1[-1]):
                if (j == 1) and (i == 'одна'):
                    cam += i
                    cam += ' десятая'
                elif (j == 2) and (i == 'две'):
                    cam += i
                    cam += ' десятых'
                elif (j >= 3):
                    cam += i
                    cam += ' десятых'
        return cam
    elif len(pa1) == 4:
        pa2 = pa1[2:]
        z = False
        for i, j in parts_number2.items():
            if int(pa2) == j:
                cam += i
                cam += ' сотых'
                z = True
        if z == True:
            return cam

        if pa2[0] == '0':
            for i, j in nat_numbers.items():
                if j == int(pa1[-1]):
                    if (j == 1) and (i == 'одна'):
                        cam += i
                        cam += ' сотая'
                    elif (j == 2) and (i == 'две'):
                        cam += i
                        cam += ' сотых'
                    elif (j >= 3):
                        cam += i
                        cam += ' сотых'
            return cam
        else:
            km = pa2[0]
            km += '0'
            for i, j in nat_numbers.items():
                if j == int(km):
                    cam += i
                    cam += ' '
            if int(pa1[-1]) != 0:
                for i, j in nat_numbers.items():
                    if j == int(pa1[-1]):
                        if (j == 1) and (i == 'одна'):
                            cam += i
                            cam += ' сотая'
                        elif (j == 2) and (i == 'две'):
                            cam += i
                            cam += ' сотых'
                        elif (j >= 3):
                            cam += i
                            cam += ' сотых'
            return cam
    elif len(pa1) == 5:
        pa2 = pa1[2:]
        if pa2[0] == '0':
            if pa2[1] == '0':
                for i, j in nat_numbers.items():
                    if j == int(pa1[-1]):
                        if (j == 1) and (i == 'одна'):
                            cam += i
                            cam += ' тысячная'
                        elif (j == 2) and (i == 'две'):
                            cam += i
                            cam += ' тысячных'
                        elif (j >= 3):
                            cam += i
                            cam += ' тысячных'
                return cam
            else:
                w = False
                for i, j in parts_number2.items():
                    if int(pa2) == j:
                        cam += i
                        cam += ' тысячных'
                        w = True
                if w == True:
                    return cam

                km = pa2[1]
                km += '0'
                for i, j in nat_numbers.items():
                    if j == int(km):
                        cam += i
                        cam += ' '
                if int(pa1[-1]) != 0:
                    for i, j in nat_numbers.items():
                        if j == int(pa1[-1]):
                            if (j == 1) and (i == 'одна'):
                                cam += i
                                cam += ' тысячная'
                            elif (j == 2) and (i == 'две'):
                                cam += i
                                cam += ' тысячных'
                            elif (j >= 3):
                                cam += i
                                cam += ' тысячных'
                return cam
        else:
            kms = pa2[0]
            kms += '00'
            for i, j in nat_numbers.items():
                if j == int(kms):
                    cam += i
                    cam += ' '
            q = False
            for i, j in parts_number2.items():
                if int(pa2) == j:
                    cam += i
                    cam += ' тысячных'
                    q = True
            if q == True:
                return cam

            if (int(pa2[1]) == 0) and (int(pa1[-1]) != 0):
                for i, j in nat_numbers.items():
                    if j == int(pa1[-1]):
                        if (j == 1) and (i == 'одна'):
                            cam += i
                            cam += ' тысячная'
                        elif (j == 2) and (i == 'две'):
                            cam += i
                            cam += ' тысячных'
                        elif (j >= 3):
                            cam += i
                            cam += ' тысячных'
                return cam
            elif (int(pa2[1]) != 0) and (int(pa1[-1] != 0)):
                km = pa2[1]
                km += '0'
                for i, j in nat_numbers.items():
                    if j == int(km):
                        cam += i
                        cam += ' '
                if int(pa1[-1]) != 0:
                    for i, j in nat_numbers.items():
                        if j == int(pa1[-1]):
                            if (j == 1) and (i == 'одна'):
                                cam += i
                                cam += ' тысячная'
                            elif (j == 2) and (i == 'две'):
                                cam += i
                                cam += ' тысячных'
                            elif (j >= 3):
                                cam += i
                                cam += ' тысячных'
                return cam


def number_desformation(number):  # вводим функцию, преобразующую целое число в строку названия этого числа (цифры)
    nummbers = []
    nuber = number

    nuber1, nuber2 = 0, 0
    if (nuber >= 100):
        nuber2 = nuber % 1000  # разбиваем исходное число по цифрам и внутренним составляющим
    if (nuber % 100 != 0):
        nuber1 = nuber % 100
    else:
        nuber1 = 0

        # далее проходимся по словарю и по частям добавляем в список названия внутренних составляющих исходного числа
    for i, j in russian_number_system.items():
        if (nuber >= 1000) and (j == (nuber - nuber2)):
            nummbers.append(i)
        elif (j == (nuber2 - nuber1)) and (nuber >= 100):
            nummbers.append(i)
        elif ((j == (nuber1 - (nuber1 % 10))) or ((11 <= j <= 19) and (j == nuber1))) and (
                (10 <= nuber1 <= 99) or (nuber1 == 10) or (nuber1 == 11) or (nuber1 == 12) or (nuber1 == 13) or (
                nuber1 == 14) or (nuber1 == 15) or (nuber1 == 16) or (nuber1 == 17) or (nuber1 == 18) or (
                        nuber1 == 19) or (nuber1 == 20) or (nuber1 == 30) or (nuber1 == 40) or (nuber1 == 50) or (
                        nuber1 == 60) or (nuber1 == 70) or (nuber1 == 80) or (nuber1 == 90)):
            nummbers.append(i)
            if ((nuber1 % 10) in decimal_words1) and (nuber1 >= 20):
                g = nuber1 % 10
                nummbers.append(decimal_words1[g])
            break
        elif (j == nuber1 % 10) and (nuber1 < 10):
            nummbers.append(i)
            if (i == 'одна') or (i == 'две'):
                del nummbers[-1]
    if nuber1 == 0:
        if nuber >= 100:
            del nummbers[-1]  # убираем название "ноль", если исходное число - 100, 200 и так далее...
    con = ' '.join(nummbers)
    return con


def calcul(stroka):  # вводим функцию, отвечающую за базовые функции калькулятора
    pa = re.compile('\w+')
    num_words = pa.findall(stroka)  # повторно преобразуем из строки слов список слов с помощью регулярных выражений
    evn = 0
    evn1 = 0
    print(num_words)

    addt1 = True
    for k in num_words:
        if k in parts_number:  # проверка наличия дробных частей в списке строк
            addt1 = False

    if addt1 == False:
        zax = num_words.index('и')
        zax += 1
        zax1 = num_words[zax:]
        zax2 = []
        for po in zax1:
            if po in operations:
                break
            else:
                zax2.append(po)
        evn = number_formation(zax2)

    if addt1 == False:
        num_words1 = num_words[::-1]
        zax = num_words1.index('и')
        zax1 = num_words1[:zax]
        zax11 = zax1[::-1]
        zax2 = []
        for po in zax11:
            zax2.append(po)
        if zax11[-1] in nat_numbers:
            zax2 = []
            zax2.append(zax11[-2])
            zax2.append(zax11[-1])
        evn1 = number_formation(zax2)

    x = []  # создаём 2 списка двух введённых чисел и преобразуем их в числа с помощью функции
    x.append(num_words[0])
    x.append(num_words[1])
    y = []
    if addt1 == False:
        for i in range(len(num_words)):
            if num_words[i] == 'и':
                iny = i
                break
        del num_words[iny]
        if 'и' in num_words:
            cx = num_words.index('и')
            num_words2 = num_words[:cx]
            y.append(num_words2[-2])
            y.append(num_words2[-1])
        else:
            y.append(num_words[-2])
            y.append(num_words[-1])
    else:
        y.append(num_words[-2])
        y.append(num_words[-1])

    x1 = number_formation(x)
    if evn != 0:
        x1 += evn
    y1 = number_formation(y)
    if evn1 != 0:
        if evn1 < 1:
            y1 += evn1

    num_words[0] = x1  # вставляем в исходный список получившиеся из строк числа
    num_words[-1] = y1
    print(num_words)

    result = 0
    if 'плюс' in num_words:  # выполняем базовые операции с целыми числами
        result = num_words[0] + num_words[-1]
        result2 = round(result, 4)
        rs = round(result, 3)
        reds = str(result2)
        if int(reds[-1]) >= 5:
            rs += 0.001
        result2 = rs
    elif 'минус' in num_words:
        result = num_words[0] - num_words[-1]
        result2 = round(result, 4)
        rs = round(result, 3)
        reds = str(result2)
        if int(reds[-1]) >= 5:
            rs += 0.001
        result2 = rs
    elif 'умножить' in num_words:
        result = num_words[0] * num_words[-1]
        result2 = round(result, 4)
        rs = round(result, 3)
        reds = str(result2)
        if int(reds[-1]) >= 5:
            rs += 0.001
        result2 = rs
    elif 'возвести' in num_words:
        result = num_words[0] ** num_words[-1]
        result2 = round(result, 4)
        rs = round(result, 3)
        reds = str(result2)
        if int(reds[-1]) >= 5:
            rs += 0.001
        result2 = rs
    elif 'разделить' in num_words:
        result = num_words[0] / num_words[-1]
        result2 = round(result, 4)
        rs = round(result, 3)
        reds = str(result2)
        if int(reds[-1]) >= 5:
            rs += 0.001
        result2 = rs
    elif 'остаток' in num_words:
        result = num_words[0] % num_words[-1]
        result2 = round(result, 4)
        rs = round(result, 3)
        reds = str(result2)
        if int(reds[-1]) >= 5:
            rs += 0.001
        result2 = rs

    print(result2)
    if result2 < 0:
        print('минус', end=' ')
        result22 = abs(result2)
    else:
        result22 = result2
    result2_1 = int(result22)
    if result2_1 == 0:
        print('ноль и', end=' ')
        opa = 0
    else:
        opa = number_desformation(result2_1)
    result2_2 = round(result22 - int(result22), 3)
    if result2_2 != 0:
        opa_1 = number_part_desf(result2_2)
    else:
        opa_1 = 0

    if (opa != 0) and (opa_1 != 0):
        print(opa, opa_1, sep=' и ')
    elif opa_1 != 0:
        print(opa_1)

    if result2 < 10000:
        print(number_desformation(result22))
    elif result22 == 10000:
        print('десять тысяч')
    else:
        print('Ошибка!')
calcul(stroka)