'''
Функции a.k.a. Процедуры a.k.a. Методы в Python

Именованные участки кода, которые можно вызывать по имени, т.е. не писать N строк кода, а написать 1, которая определяет/объединяет эти 
N строк в себе.


Шаблон для создания:
def имя_функции(параметры, через, запятую = можно_указать_стартовое_значение_параметра):
    тело
    функции
    с отступами

Бывают 2 видов: 
    * Возвращаемые (функция);
    * Невозвращаемые (процедура);

Касаемо классификации очень часто спорят, называют вещи по-разному, но принято считать:
    * Функция - подпрограмма, выполняющая какие-либо операции и возвращающая значение.
    * Процедура - подпрограмма, которая только выполняет операции, без возврата значения.
    * Метод - это функция или процедура, которая принадлежит классу или экземпляру класса

Функция должна вернуть что-то туда, где её вызвали.
Например, если мы заказываем торт у кондитера, он должен нам вернуть результат своей деятельности, т.е. тортик.
Чтобы функция вернула какое-то значение или объект, необходимо написать что нужно вернуть после слова return
Пример:
'''

# Функция, которая вернёт сумму 2 чисел, которые ей предадут
def Sum(a, b):      # Объявляем функцию Sum с 2 параметрами a, b
    return a + b    # Возвращаем сумму этих 2 параметров

v = Sum(5, 8)       # В переменную v записываем значение, которое вернёт функция Sum с параметрами 5 и 8

'''
Процедура не должна ничего возвращать, а только делать какое-то действие.
Например, если мы заказываем уборку квартиры, то горничная ничего нам не возвращает, а только убирается, и мы
получаем результат её работы не в прямом смысле.
Пример:
'''

# Процедура, которая выводит какую-то информацию об условном пользователе
def Info():                                                         # Определяем процедуру с именем Info
    print('Информация о пользователе №3221 Иванов Иван Иванович')   # Выводим строку с информацией
    print('Имя: иванов Иван Иванович')                              # Выводим строку с информацией
    print('Возраст: 34')                                            # Выводим строку с информацией 
    print('Город: Сараево')                                         # Выводим строку с информацией
    print('Род деятельности: Строитель')                            # Выводим строку с информацией

Info()                                                              # Вызываем функцию Info

# Процедура выведет текст, но в место, где её вызывали (50 строка), она никакое значение или объект не вернёт

'''
Процедура не должна ничего возвращать, а только делать какое-то действие.
Например, если мы заказываем уборку квартиры, то горничная ничего нам не возвращает, а только убирается, и мы
получаем результат её работы не в прямом смысле.
Пример:
'''

def DoPizza(a = 0, b = 0, c = 0, d = 0):        # Объявляем функцию DoPizza с 4 параметрами, все изначально равны 0
    print("Do pizza...")                        # Просто выводим текст
    print("Do pizza...")                        # Просто выводим текст
    print("Do pizza...")                        # Просто выводим текст
    print(a, b, c, d)                           # Просто выводим все переменные через пробел
    v = a+b+c+d                                 # Переменная для суммы всех 4 параметров
    return v                                    # Возвращаем значение переменной v

print(DoPizza(1, d=8))                          # Выводим на экран результат функции DoPizza, где заданы параметры a = 1, d = 8

'''
В общих словах, в 9 строчке напишется то, что вернёт функция, в данном случае это сумма всех параметров, но поскольку мы подаём изменённые 
параметры a и d, то он вернёт не 0, как это было бы при вызове DoPizza(), а 9

Если в функции указаны стартовые значения (как в строчке 61), а при вызове функции мы указываем другие значения определённых параметров (как 
в строчке 69), то стартовые значения перепишутся на указанные, не трогая остальные, т.е. мы задали a и d, а параметры b и c не меняются.
'''