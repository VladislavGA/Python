def user_info(**kwargs):
    """
    Функция возвращает кортеж значений из
    Можно ли допустить к работе?
    Оповещение следующего отдела).
    was_ill - болел ли короной
    пример возвращаемых данных (True) (False KFC)
    :return:
    """
    if kwargs['temperature'] > 36.6 and kwargs['was_ill']:
        return (False)
    elif kwargs['temperature'] > 36.6 and not kwargs['was_ill']:
        return  (False, kwargs['work_place'])
    else:
        return (True)

def update_work(user_dict)

user_dict = {'name': 'Basil',
             'age': 25,
             'temperature': 36.6,
             'work_places': ['KFC', 'Burger King', 'kofe'],
             'was_ill': False,
             'work_place': "Book"}

print(user_info(**user_dict))
user_info_data = ()

'''def user_info(*args):
    print(args, type(args))
    for arg in args:
        arg = str(arg) + '!'
        print("We Have this info: ", *args) # *args специальный символ

print(*user_info_data)
user_info('Vasil', 25, 36.7, 'KFC')'''

"""print(user_chek('Basil', 38.4, 'KFC', False))
print(user_chek('Vasil', 38.4, 'KFC', True))
print(user_chek('Kiril', 36.6, 'KFC', False))
print(user_chek('Katya', 36.6, 'KFC', True))"""