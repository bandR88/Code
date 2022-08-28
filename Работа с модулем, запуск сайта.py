import os #модуль взаимодействия системы

sayt = input() #переменная для использования ввода с клавиатуры

#далле следуют проверки по вводу имени сайта

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

