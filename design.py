from tkinter import *
from tkinter import filedialog
from decode import decode
from record import record, clean_file
from pathlib import Path
import time
from tkinter import messagebox

history = ""


# чистка истории(огромный костыль)
def clean_history():
    global history
    history = ""
    label_2 = Label(text='                                                                     \
                                                           ', justify=LEFT, background="#9D9FFF")
    label_2.place(x=10, y=50)
    label_3 = Label(text='                                                                     \
                                                           ', justify=LEFT, background="#9D9FFF")
    label_3.place(x=10, y=70)
    label_4 = Label(text='                                                                     \
                                                           ', justify=LEFT, background="#9D9FFF")
    label_4.place(x=10, y=90)
    label_5 = Label(text='                                                                     \
                                                           ', justify=LEFT, background="#9D9FFF")
    label_5.place(x=10, y=110)
    label_6 = Label(text='                                                                     \
                                                           ', justify=LEFT, background="#9D9FFF")
    label_6.place(x=10, y=130)
    label_7 = Label(text='                                                                     \
                                                           ', justify=LEFT, background="#9D9FFF")
    label_7.place(x=10, y=150)
    label_8 = Label(text='                                                                     \
                                                           ', justify=LEFT, background="#9D9FFF")
    label_8.place(x=10, y=155)


# загрузка файлов в приложение
def UploadAction(event=None):
    global history
    # принимаем путь к файлу
    filename = filedialog.askopenfilename()
    try:
        text = decode(filename)
        # проверка на тип файла
        if str(filename).split('.')[1] in ['mp3', 'ogg']:
            # запись результата в переменную и файл
            # если decode выдал ошибку, говорим об этом пользователю
            if text == 'format error':
                history += "данный формат файла не подходит(длина аудио больше \n 30 секунд или слова не опознаны) \n"
            else:
                # самые частые ошибки не произошли и мы скорее всего записали данные
                history += "Записано в файл text.txt! \n"
            record(text)
        else:
            # запись в переменную ошибки
            history += 'Данный тип файла не соответствует формату mp3 или ogg( \n'
    except IndexError:
        pass
    # выводим всю историю запросов)
    label2 = Label(text=history, justify=LEFT, background="#9D9FFF")
    label2.place(x=10, y=50)


# инфа о приложении
def butt_click():
    messagebox.showinfo(title='Помощь', message='Данное приложение может декодировать ваше голосовое сообщение '
                                                'и создать план для блок схемы.\n'
                                                'Условия для файла - он должен быть короче'
                                                ' 30 секунд и иметь формат mp3 или ogg. \n'
                                                'Чем более четко вы будете говорить слова, \n '
                                                'тем точнее будет план блок схемы')


# создание окна
root = Tk()
root.title("Компьютерный транскрайбер")
root.geometry("520x228")
root.resizable(width=False, height=False)
root.iconbitmap(r'icon.ico')
root["bg"] = "#9D9FFF"

# text history
label1 = Label(text='История:', justify=LEFT, font="20", background="#9D9FFF")
label1.place(x=10, y=10)

# buttons
btn = Button(text="Открыть", background="#5331FE", foreground="#ccc",
             padx="20", pady="8", font="16", command=UploadAction)
btn.place(x=450, y=80, anchor="c", height=120, width=100, bordermode=OUTSIDE)

btn2 = Button(text="Помощь", background="#C3BAF2", command=butt_click,
              padx="14", pady="7", font="13")
btn2.place(x=450, y=200, anchor="c", height=40, width=90)

btn3 = Button(text="Очистить файл", background="#FF9F9F",
              padx="14", pady="7", font="13", command=clean_file)
btn3.place(x=10, y=180, height=40, width=150)

btn4 = Button(text="Очистить историю", background="#FF9F9F",
              padx="14", pady="7", font="13", command=clean_history)
btn4.place(x=170, y=180, height=40, width=175)

# пасхал0чка
vk = Label(text='Создатели: https://vk.com/egor_mishalkin \
  https://vk.com/timofei_tereschenko ', justify=LEFT, font="20", background="#D3D3D3")
vk.place(x=600, y=50)

root.mainloop()
