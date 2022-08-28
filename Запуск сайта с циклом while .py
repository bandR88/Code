import os

while True:
    sayt = input('Веедите адрес сайта:\n')

    if sayt == 'стоп':
        break

    if 'https://' in sayt:
        os.system('start ' + sayt)
        print('if')

    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.system('start ' + sayt)
        print('elif')

    else:
        sayt = 'https://www.' + sayt
        os.system('start ' + sayt)
        print('else')

