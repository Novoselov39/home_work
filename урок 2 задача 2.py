
sentens = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
i = 0
for elements in sentens:
    if elements.isdigit():
        sentens[i] = ''.join (['"', elements.zfill(2),'"'])
    elif elements[1:].isdigit() and elements[0] == '+' or elements[0] == '-' in elements:
        sentens[i] = ''.join (['"', elements.zfill(3),'"'])
    i += 1
print(' '.join (sentens))