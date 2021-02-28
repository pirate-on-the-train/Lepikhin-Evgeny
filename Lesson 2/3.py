from openpyxl import load_workbook          # Импортируем метод load_book из модуля openpyxl
wb = load_workbook(filename = 'test.xlsx')  # Создаём переменную wb для работы с книгой и записываем в неё книгу с именем test.xlsx
sheet_ranges = wb['Sheet']                  # Получаем лист с названием 'Sheet' и записываем в переменную sheet_ranges
b = sheet_ranges['A4'].value                # Создаём переменную b и записываем туда значение ячейки A4 листа sheet_ranges
print(b)                                    # Выводим в консоль значение переменной b