
array = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in array:
    print('Привет', ''.join([el.split(' ')[-1].title(),'!']))

