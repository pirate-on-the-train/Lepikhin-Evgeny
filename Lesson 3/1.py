from openpyxl import Workbook                                           # Импортируем класс Workbook из модуля openpyxl
from openpyxl.chart import (AreaChart, Reference)                       # Импортируем классы AreaChart, Reference из модуля openpyxl.chart

wb = Workbook()                                                         # Создаём переменную wb для работы с книгой
ws = wb.active                                                          # Создаём переменную ws, в которую записываем активный лист (т.е. первую)

rows = [                                                                # Список rows состоящий из 7 других списков 
    ['Number', 'Batch 1', 'Batch 2'],                                   # 1 строка таблицы
    [2, 40, 30],                                                        # 2 строка таблицы 
    [3, 40, 25],                                                        # 3 строка таблицы
    [4, 50, 30],                                                        # 4 строка таблицы
    [5, 30, 10],                                                        # 5 строка таблицы
    [6, 25, 5],                                                         # 6 строка таблицы
    [7, 50, 10],                                                        # 7 строка таблицы
]

for row in rows:                                                        # Для каждого элемента row в списке rows
    ws.append(row)                                                      # На лист ws добавили каждую строку row

chart = AreaChart()                                                     # Создаём объект графика
chart.title = "Area Chart"                                              # Задаём ему заголовок
chart.style = 13                                                        # 
chart.x_axis.title = 'Test'                                             # Задаём заголовок оси x
chart.y_axis.title = 'Percentage'                                       # Задаём заголовок оси y

cats = Reference(ws, min_col=1, min_row=2, max_row=7)                   # Задаём значения для оси x
data = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=7)        # Задаём данные для графика
chart.add_data(data)                                                    # Добавляем данные в график
chart.set_categories(cats)                                              # Добавляем графику подписи

ws.add_chart(chart, "A10")                                              # Добавляем график в ячейку A10

wb.save('area.xlsx')                                                    # Сохраняем файл