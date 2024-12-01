# import json
# import urllib.request
# import webbrowser

import string # для работы с strip() | whitespace punctuation
# from calendar import weekday

# from multiprocessing.context import SpawnProcess

letters = 'asdfghjqwrrtewtreyujjb'
len(letters) # считает кол-во символы
print(letters[::-1]) # Индекс числа. Начало : Конец : Шаг | пример от начала до конца и с шагом -1 это реверс текста


tasks = 'тексты бывают, разные черные белые красные'
print(tasks.split()) # делит единый текст на куски | в аргументы принимает разделитель или любой символ если пустой


crypto_list = ['Yeti', 'Bigfoot', 'Loch ness']
crypto_string = ' - '.join(crypto_list) # Соединяет список указывает разделитель и вызывает в join список
print(crypto_string)


setup = 'a duck goes into a bar'
print(setup)
print(setup.replace('duck', 'duckie')) # находим ключ изменяем на второй параметр
print(setup.replace('a ', 'a famous ', 100)) # количество повторений в 3 параметре


world = '   earth!.? '
print(world.strip()) # устраняет отступы
print(world.strip(' ')) # устраняет символ указанный в скобках
print(world.lstrip(' ')) # устраняет символы слева
print(world.rstrip()) # устраняет символы справа
print(world.strip(' !.?' )) # устраняет указанный символ

blurt = 'what the...!!?'
print(blurt.strip(string.punctuation)) # устраняет пунктуации из импора string библиотеки

prospector = 'What in tarnation ...??!!'
print(prospector.strip(string.whitespace + string.punctuation)) # устраняет пунктуации и отступы


poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All that doth')) # начинается ли
print(poem.endswith('Hui')) # заканчивается ли

word = 'the'
print(poem.find(word)) # Поиск подстроки в строке. Если подстроки нет find выдаст -1
print('index:', poem.rindex(word)) # Так же принимет rfind и rindex. Если подстроки нет выдаст исключение
print(poem.count(word)) # Считает количество сколько раз встречается сочетание букв
print(poem.isalnum()) # являются ли символы в строке цифрами?

# text transform
print(setup.capitalize()) # первое слово с большой буквы
print(setup.title()) # Каждое слово с большой буквы
print(setup.upper()) # UPPERCASE
print(setup.lower()) # lowercase
print(setup.swapcase()) # Регистр на противоположный

# Выравнивание строк
print(setup.center(30)) # слева и справа 30 пробелов
print(setup.ljust(10)) # слева 10 пробелов
print(setup.rjust(2)) # справа 2 пробела

think = 'wereduck'
place = 'in a bar'
print(f'The {think} is in {place}')
print(f'The {think.capitalize()} is in {place.rjust(10)}') # интерполяция
print(f'The {think:>20} is in {len(poem)} and {place:!^20}') # ширина >, заполнитель ^, выравнивание
print(f'{think=}, {len(poem[:-1]) =}, {word.upper()}') # выведет значение переменной в интерполяции так же принимет выражение

answer = [
    'huinya answer', 'second huinya answer', 'third huinya answer'
]
print(answer[1])

# while True: # бесконечный цикл
#     stuff = input('Type q for exit or type text for format capitalize: ')
#     if stuff == 'q':
#         break
#     print(
#         stuff.capitalize()
#     )

# while True:
#     value = input('intager: ')
#     if value == 'q': # ввел q вышел
#         break
#     number = int(value)
#     if number % 2 == 0: # нечетное число
#         continue # пропускаем итерации, используя оператор continue
#     print(number, 'is even', number*number)

numbers = [1, 3, 5]
position = 0
while position < len(numbers): # 0 < len() считает количество данных в списке. 3 в данном случае.
    number = numbers[position] # вызываем number[1] и присваеваем его переменной number
    if number % 2 == 0: # если number четное, то вывести результат
        print('Found ', number)
        break
    position += 1 # если все норм, то присвоем след индекс
else: # break не вызываем
    print('Not found')

word = 'herui'
for letter in word:
    if letter == 'm':
        break
    print(letter)
else:
    print('No u')

# for x in range(10, -1, -1):
#     print(x)

list1 = [3, 2, 1, 0]
for number in list1:
    if number == 4:
        break
    print(number)
else:
    print('ok')




# КОРТЕЖИ И СПИСКИ

example_tuple = 'Кортеж 1', 'Ananothr Two', 'Another Three' # кортеж не изменяемый
print(type(example_tuple)) # функция вызова типа

marx_tuple = ('Family', 'Name', 'Male')
a, b, c = marx_tuple
print(a, b)

password = 'huipas'
icecream = 'tuttifrutti'
password, icecream = icecream, password # обмен значениями без создания временной переменной
print(password, icecream)

marx1_tuple = ['Family', 'Name', 'Male' ]
tuple(marx1_tuple) # преобразуем другой объект в кортеж
print(marx1_tuple) #
print(type(marx1_tuple))



# Списки
empty_list = [ ]
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_name = ['Graham', 'John', 'Jane']
leap_years = [2000, 2004, 2008, 2012, 2016, 2020]
randomness = ['Punxstatawnery', {"groundhog": "Phil"}, "Feb. 2"]

print(randomness[1])

another_empty_list = []
print(another_empty_list)

another_empty_list += ['test', 'hui']
print(another_empty_list)

print(list('hui'))

a_tuple = (1, 2, 3)
print(type(list(a_tuple)))

talk_like_a_pirate_day = '9/12/2023'
print(talk_like_a_pirate_day.split('/'))

test_list = ['Test1', 'Test2', 'Test3']
print(test_list[:2])

test_list.reverse() # Функция reverse() изменяет список, но не возвращает его значения.
print(test_list)

test_list.append('Huinyaaaa') # добавляем элемент в конец списка
print(test_list)

test_list.insert(1, 'Vashehiioudsaoidh') # Добавляем элемент на определенное место с помощью функции insert()
print(test_list)

others_guy = ['Pezda', 'Hui']
test_list.extend(others_guy) # Объединяем списки с помощью метода extend() или оператора +
print(test_list)

test_list[1] = 'Nihuyasebe' # Изменяем элемент с помощью конструкции [смещение]
print(test_list)

test_list[1:5] = [8, 9] # Изменяем элементы с помощью разделения
print(test_list)

del test_list[-1] # Удаляем заданный элемент с помощью оператора del является оператором Python, а не методом списка
print(test_list)

test_list.remove('Pezda') #  Удаляем
print(test_list)

test_list.append('6798')
print(test_list)

test_list.pop(2) #Получаем и удаляем заданный элемент с помощью функции pop()
print(test_list)

example_var = ['test1', 'test2', 'test3']
# example_var.clear() # удаляет все элементы
print(example_var.index('test2')) # index элемента | Если значение встречается в списке более одного раза, возвращается смещение только первого найденного элемента:

print('test2' in example_var) # проверяем наличие элемента в списке

example_var.insert(0, 'test3')
print(example_var.count('test3')) # count() считаем кол-во повторений значений

print(', '.join(example_var)) # преобразуем в список -- противоположность .split()

sorted_example = sorted(example_var) # sorted сортировка копии
print(sorted_example)

example_var.sort(reverse=True) # Сортирвка изменяя порядок списка. Пустой аргумент reverse=False
print(example_var)


a = [1, 2, 3, 4, 'a']
b = a.copy() # Копируем список - а | DEEPCOPY копируем словари кортежи вложенные списки. Нужно импортировать import copy
hui = list(a) # функции преобразования list
d = a[:2] # разделения списка [:]
print(d)

for example in example_var:
    print(example)

for example in example_var:
    if example.startswith('h'):
        print('All Ok this code is work')
        break
    elif example.startswith('a'):
        print('Huilan')
    else:
        print('Not Ok')

days = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
number_day = 1, 2, 3, 4, 5, 6, 7

for day, number in zip(days, number_day): # параллельное итерирование по нескольким последовательностям с помощью функции zip():
    print(day, number)

print(list(zip(days, number_day))) # список с составлением последовательности | dict(zip(var, var)) это словарь

number_list = [number-1 for number in range(1,6)] # списковых включений | [выражение for элемент in итерабельный объект]
print(number_list)

a_list = [number for number in range(1,6) if number % 2 == 1] #
print(a_list)




# 8 ГЛАВА, Словари и множества

bierce = { # Словарь из списка {} ассоциативные массивы, хешами или хеш-таблицей.
    'day': 'A period of twenty-four hours, mostly misspent',
    'positive': 'Mistaken at the top of ones voice',
    'misfortune': 'The kind of fortune that never misses',
    }
print(
    bierce['day'],
    bierce['positive'],
    bierce['misfortune'],
    sep='\n'
)

acme_customer = {'first': 'Wile', 'last': 'Coyote'} # Традиционные способ создания словаря
print(
    acme_customer['first'],
    acme_customer['last'],
)

acme_customer = dict(first="While", middle="E", last="Coyote") # с помощью dict | Ограничения - имена аргументов должны представлять собой корректные имена переменных (в них не должны использоваться пробелы и ключевые слова)
print(acme_customer['last'])

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol)) # Преобразуем с помощью функции dict() | любую последовательность, содержащую последовательности из двух элементов

acme_customer['first'] = 'hui' # перезаписываем значение в словаре
print(acme_customer)

print(
    acme_customer.get('hui') # .get получает ключ / если нет то вместо исключения выведет опциональное значение
)

print(
    acme_customer.keys() # получаем все ключи
)

print(
    list(acme_customer.keys()) # переводим ключи в список / список сохраняется в память в то врем как dict_keys создает временное значение
)

print(
    list(acme_customer.values()) # Получаем из списка значение. Вместо ключа
)

print(
    list(acme_customer.items()) # Получаем все пары ключ - значение. Пара БУДЕТ ВОЗВРАЩЕНА В КОРТЕЖЕ
)

first_constr = {'a': 'agony', 'b': 'boredom', 'c': 'calmness'}
second_constr = {'a': 'delight', 'e': 'enthusiasm', 'f': 'fun'}
print({**first_constr, **second_constr}) # объеденяем словари с помощью конструкции | эти копии являются поверхтностынми

first_constr_dop = {'x': 'dsads', 'v': 'adsf'}

first_constr.update(first_constr_dop) # Объединяем словари с помощь update()
print(first_constr)

drink = {
    'martini': {'vodka', 'gin', 'rum'},
    'whisky': {'vodka', 'vermouth', 'tequila'},
    'beer': {'beer', 'wine', 'rak'}
}

for name, contents in drink.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drink.items():
    if 'vodka' in contents and not ('wine' in contents or 'rak' in contents):
        print(name)



e2f = {
'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'
}
print(e2f)