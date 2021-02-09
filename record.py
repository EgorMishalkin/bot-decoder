# слова с базовыми словами, которые не должны писаться в неопознанных
words = ['вот', 'ввод', 'переменная', 'параллелограм', 'значение', 'переменный', 'вывод', 'вывести', 'выводи',
                 'вывод', 'вывести', 'выводи', 'конец', 'завершить', 'завершение', 'закончить',
                 'действие', 'действия' 'выполнить']


# чистка файла
def clean_file():
    global words
    # открываем, чистим, закрываем. чистим словарь от лишних слов
    f = open('text.txt', "r+", encoding='utf8')
    f.truncate()
    f.close()
    words = ['вот', 'ввод', 'переменная', 'параллелограм', 'значение', 'переменный', 'вывод', 'вывести', 'выводи',
             'вывод', 'вывести', 'выводи', 'конец', 'завершить', 'завершение', 'закончить',
             'действие', 'действия' 'выполнить']


def record(text):
    global words
    f = open('text.txt', "a", encoding='utf8')

    # сразу записываем если ошибка в передачи файла
    if text == 'format error':
        f.write(f'данный формат файла не подходит(длина аудио больше 30 секунд или слова не опознаны) \n')
    else:
        # номер действия
        action = 1
        text = text.lower().split(' ')
        miss_word = ''

        # начинаем анализировать полученный текст
        for numb, word in enumerate(text):
            act = False
            # если старт то начинаем
            if word in ['начать', 'начало', 'старт', 'овал']:
                f.write(f'{action}) начало \n')
                action += 1
                act = 1

            # ввод значений
            if word in ['вот', 'ввод', 'переменная', 'параллелограм', 'значение', 'переменный']:
                # некоторые говорят 'ввод переменной икс'б а кто-то 'ввод'. Учтем оба варианта
                if text[numb + 1] in ['переменной', 'переменная']:
                    f.write(f'{action}) ввод переменной {text[numb + 2]} \n')
                    action += 1
                    act = 1
                    print(text[numb + 2])
                    words.append(text[numb + 2])
                else:
                    f.write(f'{action}) ввод переменной {text[numb + 1]} \n')
                    action += 1
                    act = 1
                    words.append(text[numb + 1])

            # ввыод переменной. все так же как и ввод
            if word in ['вывод', 'вывести', 'выводи']:
                if text[numb + 1] in ['переменную', 'переменной', 'переменная']:
                    f.write(f'{action}) вывод переменной {text[numb + 2]} \n')
                    action += 1
                    act = 1
                    print(text[numb + 2])
                    words.append(text[numb + 2])
                else:
                    f.write(f'{action}) вывод переменной {text[numb + 1]} \n')
                    action += 1
                    act = 1
                    words.append(text[numb + 1])

            # завершаем блок схему. обнуляем action
            if word in ['конец', 'завершить', 'завершение', 'закончить']:
                f.write(f'{action}) конец \n')
                action = 1
                act = 1

            if word in ['действие', 'действия' 'выполнить', 'прямоугольник']:
                a = ""
                fal = 0
                while fal == 0:
                    # проходимся по нашему словарю
                    for i in text[numb:-1]:
                        # если новое действие, то заканчиваем цикл
                        if i in words:
                            fal = 1
                        else:
                            words.append(i)
                            a += f'{i} '
                # действие
                f.write(f'{action}) выполнить {a}\n')
                action += 1
                act = 1

            if act == 0:
                if word in words:
                    pass
                else:
                    miss_word += word + ' '

        #  stroke лежит текст
        stroka = ''
        for i in text:
            stroka += f'{i} '
        f.write(f'переведенный текст - {stroka} \n')
        if miss_word != '':
            f.write(f'неопознанные слова - {miss_word} \n \n')
        else:
            f.write('неопознанных слов нет \n \n')

        f.close()
