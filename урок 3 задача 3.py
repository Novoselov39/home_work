
def thesaurus(list_):
    dict_sort = {}
    dict = {}
    list_name = []

    for name in list_:
        letter_1 = list(name)[0]
        for letter in list_:
            if list(letter)[0] == letter_1:
                list_name.append (letter)
        dict [list(name)[0]] = list_name
        list_name = []
    # сортировка списка:
    list_key = list (dict.keys())
    list_key.sort()
    for sort in list_key:
        dict_sort [sort] = dict[sort]
    return(dict, dict_sort)

thesaurus_1 = ("Тихомир", "Петр", "Мария", "Илья", "Толя", "Иван")
#print  (thesaurus(thesaurus_1)[0]) #не сортированный список
#print  (thesaurus(thesaurus_1)[1]) #сортированный список
for key, value in thesaurus(thesaurus_1)[1].items():
    print(f' "{key}": \n\t {value}')