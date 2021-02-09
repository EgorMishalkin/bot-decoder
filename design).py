from tkinter import *
from tkinter import filedialog
from decode import decode
from record import record, clean_file
from pathlib import Path
import time

history = ""


def clean_history():
    global history
    history = ""
    label2 = Label(text=history, justify=LEFT, background="#D3D3D3")
    label2.place(x=10, y=50)



def UploadAction(event=None):
    global history
    # принимаем путь к файлу
    filename = filedialog.askopenfilename()
    try:
        text = decode(filename)
        # проверка на тип файла
        if str(filename).split('.')[1] in ['mp3', 'ogg']:
            # запись результата в переменную и файл
            if text == 'format error':
                history += "данный формат файла не подходит(длина аудио больше \n 30 секунд или слова не опознаны) \n"
            else:
                history += "Записано! \n"
            record(text)
        else:
            # запись в переменную ошибки
            history += 'Данный тип файла не соответствует формату mp3 или ogg( \n'
    except IndexError:
        pass
    label2 = Label(text=history, justify=LEFT, background="#D3D3D3")
    label2.place(x=10, y=50)


def createNewWindow():
    app = Tk()

    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

    app.mainloop()


root = Tk()
root.title("Компьютерный транскрайбер")
root.geometry("540x228")
root.resizable(width=False, height=False)
root.iconbitmap(r'icon.ico')

# background
root["bg"] = "#D3D3D3"

label1 = Label(text='История:', justify=LEFT, font="20", background="#D3D3D3")
label1.place(x=10, y=10)

btn = Button(text="Открыть", background="#0000FF", foreground="#ccc",
             padx="20", pady="8", font="16", command=UploadAction)
btn.place(x=450, y=80, anchor="c", height=120, width=100, bordermode=OUTSIDE)

btn2 = Button(text="Помощь", background="#2E8B57", command=createNewWindow,
              foreground="#ccc", padx="14", pady="7", font="13")
btn2.place(x=450, y=180, anchor="c", height=60, width=100)

btn3 = Button(text="Очистить файл", background="#BA55D3",
              foreground="#ccc", padx="14", pady="7", font="13", command=clean_file)
btn3.place(x=10, y=150, height=60, width=180)

btn4 = Button(text="Очистить историю", background="#BA55D3",
              foreground="#ccc", padx="14", pady="7", font="13", command=clean_history)
btn4.place(x=200, y=150, height=60, width=180)


root.mainloop()
