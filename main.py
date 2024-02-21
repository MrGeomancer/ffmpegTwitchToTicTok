from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

path = str
photo = None  # Глобальная переменная для изображения
video_cap = None  # Глобальная переменная для каптчера видео
slider = None
path_old = str
checkboxes_entries_cs = []
checkboxes_entries_apex = []
checkboxes_entries_any = []

def resize_photo(image,canvas):
    img_width, img_height = image.size
    canvas_width, canvas_height = canvas.winfo_reqwidth(), canvas.winfo_reqheight()
    scale_x = canvas_width / img_width
    scale_y = canvas_height / img_height
    scale_factor = min(scale_x, scale_y)
    image = image.resize((int(img_width * scale_factor), int(img_height * scale_factor)))
    return ImageTk.PhotoImage(image), int(img_width * scale_factor)


def explore():
    global path
    path = filedialog.askopenfilename()
    if path == '': path = path_old
    lbl2.configure(text=path)

def prewatch(path):
    global photo
    global slider
    global path_old

    try:
        frame_show = int(slider.get())
    except:
        frame_show = 24
    canvas = Canvas(prewatch_rf, width=1080, height=720)
    canvas.grid(column=1, row=2)
    canvas.delete("all")

    video_frame = cv2.VideoCapture(path)
    video_frame.set(cv2.CAP_PROP_POS_FRAMES, frame_show-1)
    success, frame = video_frame.read()

    frame_count = int(video_frame.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(frame_rgb)
    photo, canvaslenght = resize_photo(image,canvas)

    slider_int = IntVar(value=24)



    if path != path_old:
        lbl3 = Label(prewatch_rf, text='', width=5)
        lbl3.grid(column=0, row=1)

        slider = ttk.Scale(prewatch_rf, from_=1, to=frame_count-1, orient=HORIZONTAL, length=canvaslenght, variable=slider_int,
                           command=lambda value: lbl3.config(text=slider_int.get())
                           )
        slider.grid(column=1, row=1)

    lbl4.config(text=f'{path} frame: {frame_show}')


    # print(photo.width(), photo.height())
    canvas.config(width=photo.width(), height=photo.height())
    canvas.create_image(0, 0, anchor=NW, image=photo)
    path_old = path


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")

style = ttk.Style()
style.configure('TCheckbutton', font = 20)

prewatch_rf = Frame(window)
prewatch_rf.grid(column=2, row=0, rowspan=100)

lbl = Label(window, text="Введите путь к на видео:", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

lbl2 = Label(window, text=f"", font=("Arial Bold", 12), bg='lightgray', width=50)  # отображение пути к видео
lbl2.grid(column=0, row=1)

btn = ttk.Button(window, text="Обзор..", command=explore)
btn.grid(column=1, row=1)

btn2 = Button(window, text="Предпросмотр", command=lambda: prewatch(path))
btn2.grid(column=1, row=2)

lbl4 = Label(prewatch_rf, text='')  # название видео, фрейм
lbl4.grid(column=1, row=0)


radiobtns = Frame(window)

def drowframe_cs():
    tab_apex.grid_remove()
    tab_any.grid_remove()
    tab_cs.grid(column=0, row=1, columnspan=3)

def drowframe_apex():
    tab_cs.grid_remove()
    tab_any.grid_remove()
    tab_apex.grid(column=0, row=1, columnspan=3)

def drowframe_any():
    tab_apex.grid_remove()
    tab_cs.grid_remove()
    tab_any.grid(column=0, row=1, columnspan=3)


radiobtns.grid(column=0, row=2)
rad1 = ttk.Radiobutton(radiobtns, text='CS2', value=1, command=drowframe_cs)
rad1.grid(column=0, row=0)

rad2 = ttk.Radiobutton(radiobtns, text='Apex', value=2, command=drowframe_apex)
rad2.grid(column=1, row=0, padx=20)

rad3 = ttk.Radiobutton(radiobtns, text='Any', value=3, command=drowframe_any)
rad3.grid(column=2, row=0)

tab_cs = ttk.Frame(radiobtns)
tab_apex = ttk.Frame(radiobtns)
tab_any = ttk.Frame(radiobtns)


def add_checkbox_entry_cs():
    # Создаем новый Checkbox и Entry
    checkbox = ttk.Checkbutton(tab_cs, text="Checkbox")
    entry = Entry(tab_cs, width=38)
    entry.insert(0, 'Длина, Высота, Начиная с х, Начиная с y')


    # Добавляем Checkbox и Entry в список
    checkboxes_entries_cs.append((checkbox, entry))

    # Размещаем Checkbox и Entry на форме
    checkbox.grid(row=2+len(checkboxes_entries_cs), column=0, sticky=W)
    entry.grid(row=2+len(checkboxes_entries_cs), column=1, columnspan=2, sticky=E)


def add_checkbox_entry_apex():
    # Создаем новый Checkbox и Entry
    checkbox = ttk.Checkbutton(tab_apex, text="Checkbox")
    entry = Entry(tab_apex, width=38)
    entry.insert(0, 'Длина, Высота, Начиная с х, Начиная с y')


    # Добавляем Checkbox и Entry в список
    checkboxes_entries_apex.append((checkbox, entry))

    # Размещаем Checkbox и Entry на форме
    checkbox.grid(row=2+len(checkboxes_entries_apex), column=0, sticky=W)
    entry.grid(row=2+len(checkboxes_entries_apex), column=1, columnspan=2, sticky=E)


def print_values_cs():
    # Печатаем значения всех Checkbox и Entry
    for checkbox, entry in checkboxes_entries_cs:
        print(f"Checkbox: {checkbox.state()}, Entry: {entry.get()}")


def print_values_apex():
    # Печатаем значения всех Checkbox и Entry
    for checkbox, entry in checkboxes_entries_apex:
        print(f"Checkbox: {checkbox.state()}, Entry: {entry.get()}")


chb_to916 = ttk.Checkbutton(tab_cs, text='to 9:16',padding=20)
chb_to916.grid(column=0, row=0)

chb_kills = ttk.Checkbutton(tab_cs, text='kills',padding=20)
chb_kills.grid(column=1, row=0)

chb_players = ttk.Checkbutton(tab_cs, text='players',padding=20)
chb_players.grid(column=2, row=0)

chb_radar = ttk.Checkbutton(tab_cs, text='radar',padding=20)
chb_radar.grid(column=0, row=1)

chb_crop = ttk.Checkbutton(tab_cs, text='crop')
chb_crop.grid(column=1, row=1,sticky=E)
ent_crop = ttk.Entry(tab_cs)
ent_crop.insert(0, '1200,1080,360,0')
ent_crop.grid(column=2, row=1,sticky=W)

ttk.Button(tab_cs, text='Добавить crop', command=add_checkbox_entry_cs).grid(column=1, row=2)

print_button = Button(tab_cs, text="Печать значений", command=print_values_cs)
print_button.grid(column=2, row=2, pady=5)


chb_to916 = ttk.Checkbutton(tab_apex, text='to 9:16',padding=20)
chb_to916.grid(column=0, row=0)

chb_kills = ttk.Checkbutton(tab_apex, text='kills',padding=20)
chb_kills.grid(column=1, row=0)

chb_hp = ttk.Checkbutton(tab_apex, text='hp',padding=20)
chb_hp.grid(column=2, row=0)

chb_radar = ttk.Checkbutton(tab_apex, text='radar',padding=20)
chb_radar.grid(column=0, row=1)

chb_crop = ttk.Checkbutton(tab_apex, text='crop')
chb_crop.grid(column=1, row=1,sticky=E)
ent_crop = ttk.Entry(tab_apex)
ent_crop.insert(0, '1200,1080,360,0')
ent_crop.grid(column=2, row=1,sticky=W)

ttk.Button(tab_apex, text='Добавить crop', command=add_checkbox_entry_apex).grid(column=1, row=2)

print_button = Button(tab_apex, text="Печать значений", command=print_values_apex)
print_button.grid(column=2, row=2, pady=5)




# btn = ttk.Button(radiobtns, text="Обзор..", command= lambda: print(chb_players.state(), chb_kills.state()))
# btn.grid(column=2, row=2)
#
#
# def forget():
#     chb_players.grid_forget()
#
#
# btn = ttk.Button(radiobtns, text="скрыть людей", command=forget)
# btn.grid(column=2, row=3)
#
#
# btn = ttk.Button(radiobtns, text="makeda", command=lambda:chb_players_state.set(True))
# btn.grid(column=2, row=4)


window.geometry('1800x900')
window.mainloop()
