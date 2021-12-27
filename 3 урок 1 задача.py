

def num_translate(num):
    dictionary = {'one':'один', 'two':'два', 'tree':'три', 'four':'четыре', 'five':'пять',
              'six':'шесть', 'seven':'семь','eigh':'восемь','nine':'девять','ten':'десять'}
    if not num.lower() in dictionary:
        return (None)

    if num[0].isupper():
        return dictionary[num.lower()].title()
    else:
        return dictionary[num.lower()]


example = ['one', 'Two', 'Tree', 'four', 'five',
              'six', 'seven','eigh','nine','ten']
for number in example:
    if num_translate(number) != None:
        print(number, 'переводится как:', num_translate(number))
    else: print(None)
