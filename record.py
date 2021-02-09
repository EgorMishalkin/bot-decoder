def clean_file():
    f = open('text.txt', "r+", encoding='utf8')
    f.truncate()
    f.close()


def record(text):
    f = open('text.txt', "a", encoding='utf8')

    if text == 'format error':
        f.write(f'данный формат файла не подходит(длина аудио больше 30 секунд или слова не опознаны)')
    else:
        print(text)
        action = 1
        text = text.lower().split(' ')
        miss_word = ''
        var = ['выполнить']
        # начинаем анализировать полученный текст
        for numb, word in enumerate(text):
            act = False
            if word in ['начать', 'начало', 'старт', 'овал']:
                f.write(f'{action}) начало \n')
                action += 1
                act = 1

            if word in ['вот', 'ввод', 'переменная', 'параллелограм', 'значение', 'переменный']:
                if text[numb + 1] in ['переменной', 'переменная']:
                    f.write(f'{action}) ввод переменной {text[numb + 2]} \n')
                    action += 1
                    act = 1
                    print(text[numb + 2])
                    var.append(text[numb + 2])
                else:
                    f.write(f'{action}) ввод переменной {text[numb + 1]} \n')
                    action += 1
                    act = 1
                    var.append(text[numb + 1])


            if word in ['вывод', 'вывести', 'выводи']:
                if text[numb + 1] in ['переменную', 'переменной', 'переменная']:
                    f.write(f'{action}) вывод переменной {text[numb + 2]} \n')
                    action += 1
                    act = 1
                    print(text[numb + 2])
                    var.append(text[numb + 2])
                else:
                    f.write(f'{action}) вывод переменной {text[numb + 1]} \n')
                    action += 1
                    act = 1
                    var.append(text[numb + 1])

            if word in ['конец', 'завершить', 'завершение', 'закончить']:
                f.write(f'{action}) конец \n')
                action  = 1
                act = 1

            if word in ['действие', 'выполнить']:
                f.write(f'{action}) выполнить \n')

            if act == 0:
                if word in var:
                    pass
                else:
                    miss_word += word + ' '

        stroka = ''
        for i in text:
            stroka += f'{i} '
        f.write(f'переведенный текст - {stroka} \n')
        if miss_word != '':
            f.write(f'неопознанные слова - {miss_word} \n \n')
        else:
            f.write('неопознанных слов нет \n \n')

        f.close()
