def clean_file():
    f = open('text.txt', "r+", encoding='utf8')
    f.truncate()
    f.close()


def record(text):
    f = open('text.txt', "a", encoding='utf8')

    if text == 'формат нет':
        f.write(f'данный формат файла не подходит(длина больше 30 секунд или слова не опознаны)')

    print(text)
    action = 1
    text = text.lower().split(' ')
    miss_word = ''
    # начинаем анализировать полученный текст
    for numb, word in enumerate(text):
        act = False
        if word in ['начать', 'начало', 'старт', 'овал']:
            f.write(f'{action}) начало \n')
            action += 1
            act = 1

        if word in ['вот', 'ввод', 'переменная', 'параллелограм', 'значение']:
            if text[numb + 1] in ['переменной', 'переменная']:
                f.write(f'{action}) ввод переменной {text[numb + 2]} \n')
                action += 1
                act = 1
            else:
                f.write(f'{action}) ввод переменной {text[numb + 1]} \n')
                action += 1
                act = 1

        if word in ['конец', 'завершить', 'завершение', 'закончить']:
            f.write(f'{action}) завершение схемы \n')
            action  = 1
            act = 1

        if act == 0:
            miss_word += word + ' '

    f.write(f'неопознанные слова - {miss_word} \n \n')

    f.close()
