'''Задача "Функциональное разнообразие":
Lambda-функция:
Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'
Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
Здесь ? - место написания lambda-функции.

Результатом должен быть список совпадения букв в той же позиции:
[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
Где True - совпало, False - не совпало.

Замыкание:
Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий неограниченное количество данных любого типа.
Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
Функция get_advanced_writer возвращает функцию write_everything.

Данный код:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
Запишет данные в файл в таком виде:


Метод __call__:
Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию choice из модуля random.

Ваш код (количество слов для случайного выбора может быть другое):
from random import choice
# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
Примерный результат (может отличаться из-за случайности выбора):
Да
Да
Наверное

Примечания:
Все задания пишутся в одном модуле.
Передаваемые данные в функции и объекты можете использовать свои, главное, чтобы ваш код полноценно демонстрировал логику написанного.
Файл module_9_4.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''
import random
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'



def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(f'({file_name}','w',encoding='utf-8') as file:
            data_set=str(data_set)
            file.write(data_set)
    return  write_everything


class MysticBall:
    def __init__(self,*words):
        self.words=words

    def __call__(self):
        return random.choice(self.words)

result1=list(map(lambda x,y:ord(x)==ord(y), first, second))
print(list(result1))

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Ты увурен?')
print(first_ball())
print(first_ball())
print(first_ball())