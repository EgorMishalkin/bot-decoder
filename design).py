from tkinter import *
from tkinter import filedialog
from decode import decode
from record import record, clean
from pathlib import Path

history = ""


def UploadAction(event=None):
    global history
    # принимаем путь к файлу
    filename = filedialog.askopenfilename()
    try:
        text = decode(filename)
        # проверка на тип файла
        if str(filename).split('.')[1] in ['mp3', 'ogg']:
            # запись результата в переменную и файл
            history += "Записано! \n"
            record(text)
        else:
            # запись в переменную ошибки
            history += 'Данный тип файла не соответствует формату mp3 или ogg( \n'
    except IndexError:
        pass
    label2 = Label(text=history, justify=LEFT, background="#40E0D0")
    label2.place(x=10, y=50)


root = Tk()
root.title("Компьютерный транскрайбер")
root.geometry("540x228")
root.resizable(width=False, height=False)
root.iconbitmap(r'icon.ico')

# background
root["bg"] = "#40E0D0"

label1 = Label(text='История:', justify=LEFT, font="20", background="#40E0D0")
label1.place(x=10, y=10)

# button
btn = Button(text="Открыть", background="#0000FF", foreground="#ccc",
             padx="20", pady="8", font="16", command=UploadAction)
btn.place(x=450, y=80, anchor="c", height=120, width=100, bordermode=OUTSIDE)

btn2 = Button(text="Помощь", background="#708090", foreground="#ccc", padx="14", pady="7", font="13")
btn2.place(x=450, y=180, anchor="c", height=60, width=100)

btn3 = Button(text="Очистить файл", background="#BA55D3",
              foreground="#ccc", padx="14", pady="7", font="13", command=clean)
btn3.place(x=10, y=150, height=60, width=180)

btn4 = Button(text="Очистить историю", background="#BA55D3",
              foreground="#ccc", padx="14", pady="7", font="13", command=clean)
btn4.place(x=200, y=150, height=60, width=180)


root.mainloop()