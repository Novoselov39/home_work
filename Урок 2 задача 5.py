price = [54.6, 34.90, 76.9, 44.23, 67.3, 98.23, 65.1, 76, 45, 40.31 ]
for el in price:
    if type(el) == float:
        price_el = str(el).split('.')
        print(price_el[0], 'руб', price_el[1].zfill(2), 'коп')
    elif type(el) == int:
        print(el, 'руб')
    else: print('Не верная стоимость')
