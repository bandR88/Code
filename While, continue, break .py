x = ''

while len(x) <= 5:
    y = input('Введи данные: ')
    if y == 'o':
        continue
    if y == 'l':
        break

    x +=y

else:
    print(x)

print('Программа завершена')
