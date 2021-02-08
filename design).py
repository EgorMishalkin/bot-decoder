from tkinter import *
from tkinter import filedialog


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    # проверка на тип файла
    try:
        if str(filename).split('.')[1] in ['mp3', 'ogg']:
            # print('Selected:', filename)
            label2 = Label(text=filename, justify=LEFT, background="#40E0D0")
            label2.place(relx=.2, rely=.3)
        else:
            # print('Not selected')
            label2 = Label(text='Данный тип файла не cоотетсвует \n'
                                'формату mp3 или ogg', justify=LEFT, background="#40E0D0")
            label2.place(relx=.2, rely=.3)
    except IndexError:
        pass


root = Tk()
root.title("Компьютерный транскрайбер")
root.geometry("650x250")

# root.iconbitmap(r'D:\AAA\microphone-4_icon-icons.com_62159.ico')

# background
root["bg"] = "#40E0D0"


# label1 = Label(text='Выберите файл формата \n mp3 или ogg', justify=CENTER, background="#40E0D0")
# label1.place(relx=.2, rely=.1)

# button
btn = Button(text="Open", background="#0000FF", foreground="#ccc", justify=CENTER,
             padx="20", pady="20", font="16", command=UploadAction)
btn.place(relx=.5, rely=.6, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn.pack()

root.mainloop()
