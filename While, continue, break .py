x = 'oiuooogydsfpo'
count = 0
while len(x) <= 5:
    y = input('Введи данные: ')
    if y == 'o':
        count += 1
        continue
    if y == 'l':
        break

    x +=y

else:
    print(x)

print('Программа завершена', count)
