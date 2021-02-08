def record(text):

    f = open('text.txt', "a", encoding='utf8')
    f.write(f'{text} \n')
    f.close()

