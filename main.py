from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

path = str
photo = None  # Глобальная переменная для изображения
video_cap = None  # Глобальная переменная для каптчера видео


def resize_photo(image,canvas):
    img_width, img_height = image.size
    canvas_width, canvas_height = canvas.winfo_reqwidth(), canvas.winfo_reqheight()
    scale_x = canvas_width / img_width
    scale_y = canvas_height / img_height
    scale_factor = min(scale_x, scale_y)
    image = image.resize((int(img_width * scale_factor), int(img_height * scale_factor)))
    return ImageTk.PhotoImage(image)


def explore():
    global path
    path = filedialog.askopenfilename()
    lbl2.configure(text=path)
    # lbl2.configure(width=len(path))

def prewatch(path):
    global photo
    canvas = Canvas(window, width=1080, height=720)
    canvas.grid(column=3, row=2)
    canvas.delete("all")

    image = Image.open(path)
    photo = resize_photo(image,canvas)

    Label(window, text=path).grid(column=3, row=1)
    canvas.create_image(0, 0, anchor=NW, image=photo)


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")

lbl = Label(window, text="Введите путь к на видео:", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

lbl2 = Label(window, text=f"", font=("Arial Bold", 12), bg='lightgray', width=50)
lbl2.grid(column=0, row=1)

btn = ttk.Button(window, text="Обзор..", command=explore)
btn.grid(column=1, row=1)

btn2 = Button(window, text="Предпросмотр", command=lambda: prewatch(path))
btn2.grid(column=1, row=2)



window.geometry('1800x900')
window.mainloop()
