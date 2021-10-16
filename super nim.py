from random import *
a = [[0] * 8 for i in range(8)]          # создаём пустую шахматную доску размером 8х8
for s in range(8):
    for z in range(8):
        a[s][z] = randint(0, 1)          # раскидываем фишки на пустую доску случайным образом
for i in range(8):
    print(end="\n")
    for j in range(8):
        print(a[i][j], end=" ")          # форматируем матрицу из двумерного списка
print(end='\n')
p, w, l, x, y = 2, 0, 0, 0, 0
while w != 64:
    if p == 1:          # определение игрока, делающего ход
        p = 2
    else:
        p = 1
    if p == 1:
        print()
        print('Ход 1 игрока')
    else:
        print()
        print('Ход 2 игрока')
    vh, n = input('Введите вертикаль/горизонталь '), int(input('Введите номер горизонтали/вертикали '))
    if vh == 'v':
        for q in range(8):
            if a[q][n - 1] == 1:          # проверяем наличие фишек на поле в случае, когда есть только 1 фишка на введённой вертикали и её номере
                l += 1
                x = q
            else:
                continue
        if l == 1:
            a[x][n - 1] = 0
        elif l != 0:
            for i in range(8):
                if a[i][n - 1] == 1:          # очищаем фишки на введённой с номером вертикали
                    a[i][n - 1] = 0
        l = 0
        x = 0
    if vh == 'h':
        for q in range(8):
            if a[n - 1][q] == 1:          # проверяем наличие фишек на поле в случае, когда есть только 1 фишка на введённой горизонтали и её номере
                l += 1
                y = q
            else:
                continue
        if l == 1:
            a[n - 1][y] = 0
        elif l != 0:
            for i in range(8):
                if a[n - 1][i] == 1:          # очищаем фишки на введённой с номером горизонтали
                    a[n - 1][i] = 0
        l = 0
        y = 0
    w = 0
    for i in range(8):
        for j in range(8):
            if a[i][j] == 0:          # проверяем, есть ли на поле фишки
                w += 1
    for i in range(8):
        print(end="\n")
        for j in range(8):
            print(a[i][j], end=" ")          # выставляем доску после хода игрока
    print(end='\n')
print()
print('Победил игрок ', p)          # определяем победителя