def clean():
    f = open('text.txt', "a", encoding='utf8')
    f.write('')
    f.close()


def record(text):

    f = open('text.txt', "a", encoding='utf8')
    print(text)
    action = 1
    text = text.lower().split(' ')
    for numb, word in enumerate(text):
        if word in ['начать', 'начало', 'старт', 'овал']:
            f.write(f'{action}) начало \n')
            action += 1

        if word in ['вот', 'ввод', 'переменная', 'параллелограм', 'значение']:
            if text[numb + 1] in ['переменной', 'переменная']:
                f.write(f'{action}) ввод переменной {text[numb + 2]} \n')
                action += 1
            else:
                f.write(f'{action}) ввод переменной {text[numb + 1]} \n')
                action += 1

        if word in ['конец', 'завершить', 'завершение', 'закончить']:
            f.write(f'{action}) завершение схемы \n \n')
            action  = 1

    # f.write(f'{text} \n')
    f.close()

