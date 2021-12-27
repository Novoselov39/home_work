from random import choice

def get_jokes(num):
    """Генератор шуток"""
    jokes_list = []
    for kol in range(num):
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        jokes = (choice(nouns)+" "+choice(adverbs)+" "+choice(adjectives))
        jokes_list.append(jokes)
        #print(jokes)
    return jokes_list

Numbers = int(input('Введи кол-во шуток: '))
print(get_jokes(Numbers ))

