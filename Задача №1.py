duration=int(input("duration = "))

day=duration//86400
duration=duration%86400
hour=duration//3600
duration=duration%3600
min=duration//60
sek=duration%60

if day!=0:
    print(day, 'дн', hour, 'час', min, 'мин', sek, 'c')
elif hour!=0:
    print(hour, 'час', min, 'мин', sek, 'c')
elif min != 0:
    print(min, 'мин', sek, 'c')
else:
    print(sek, 'c')