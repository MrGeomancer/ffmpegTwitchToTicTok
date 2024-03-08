from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

import gigachad2

path = str
photo = None  # Глобальная переменная для изображения
video_cap = None  # Глобальная переменная для каптчера видео
slider = None
path_old = str
checkboxes_entries_cs = []
checkboxes_entries_apex = []
checkboxes_entries_any = []


def resize_photo(image, canvas):
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


def prewatch_frame(path):
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
    video_frame.set(cv2.CAP_PROP_POS_FRAMES, frame_show - 1)
    success, frame = video_frame.read()

    frame_count = int(video_frame.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(frame_rgb)
    photo, canvaslenght = resize_photo(image, canvas)

    slider_int = IntVar(value=24)

    if path != path_old:
        lbl3 = Label(prewatch_rf, text='', width=5)
        lbl3.grid(column=0, row=1)

        slider = ttk.Scale(prewatch_rf, from_=1, to=frame_count - 1, orient=HORIZONTAL, length=canvaslenght,
                           variable=slider_int,
                           command=lambda value: lbl3.config(text=slider_int.get())
                           )
        slider.grid(column=1, row=1)

    lbl4.config(text=f'{path} frame: {frame_show}')

    # print(photo.width(), photo.height())
    canvas.config(width=photo.width(), height=photo.height())
    canvas.create_image(0, 0, anchor=NW, image=photo)
    path_old = path


def prerender_frame():
    print()
    pass


def render():
    global path
    preset = dict
    any_to916 = bool
    cs_kills = bool
    cs_players = bool
    cs_radar = bool
    any_crop = bool
    any_webcam = bool
    any_cropentry = str
    apex_kills = bool
    apex_zone = bool
    apex_radar = bool
    apex_hp = bool
    apex_hp_armor = bool
    apex_rang = bool
    apex_make_bg = bool
    outputs = []
    radval = radio_var.get()
    # print('radval:',radval)
    if radval == 1:
        chb = [chb_to916_cs,
               chb_kills_cs,
               chb_players_cs,
               chb_radar_cs,
               chb_crop_cs,
               ]

        try:
            if chb_crop_cs.state()[0] == 'selected':
                any_crop = True
                any_cropentry = ent_crop_cs.get()
                outputs.append(fr'{path}_folder/croped_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_to916_cs.state()[0] == 'selected':
                any_to916 = True
                # outputs.append(fr'{path}_folder/blured.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_kills_cs.state()[0] == 'selected':
                cs_kills = True
                outputs.append(fr'{path}_folder/kills_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_players_cs.state()[0] == 'selected':
                cs_players = True
                outputs.append(fr'{path}_folder/players_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_radar_cs.state()[0] == 'selected':
                cs_radar = True
                outputs.append(fr'{path}_folder/radar_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_webcam_cs.state()[0] == 'selected':
                any_webcam = True
                outputs.append(fr'{path}_folder/webcam_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass
    if radval == 2:
        apex_make_bg = True

        try:
            if chb_crop_apex.state()[0] == 'selected':
                any_crop = True
                any_cropentry = ent_crop_apex.get()
                outputs.append(fr'{path}_folder/croped_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_to916_apex.state()[0] == 'selected':
                any_to916 = True
                # outputs.append(fr'{path}_folder/blured.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_kills_apex.state()[0] == 'selected':
                apex_kills = True
                outputs.append(fr'{path}_folder/kills_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_zone_apex.state()[0] == 'selected':
                apex_zone = True
                outputs.append(fr'{path}_folder/zone_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_radar_apex.state()[0] == 'selected':
                apex_radar = True
                outputs.append(fr'{path}_folder/radar_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_rang_apex.state()[0] == 'selected':
                apex_rang = True
                outputs.append(fr'{path}_folder/rang_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_hp_apex.state()[0] == 'selected':
                apex_hp = True
                outputs.append(fr'{path}_folder/hp_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_hp_armor_apex.state()[0] == 'selected':
                apex_hp_armor = True
                outputs.append(fr'{path}_folder/hp_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

        try:
            if chb_webcam_apex.state()[0] == 'selected':
                any_webcam = True
                outputs.append(fr'{path}_folder/webcam_on_bg.mp4')
        except IndexError:
            # print('пустая')
            pass

    gigachad2.render(outputs=outputs,
                     any_to916=any_to916, any_crop=any_crop, any_cropentry=any_cropentry, any_webcam=any_webcam,
                     cs_kills=cs_kills, cs_players=cs_players, cs_radar=cs_radar,
                     apex_make_bg=apex_make_bg, apex_radar=apex_radar, apex_hp=apex_hp, apex_kills=apex_kills,
                     apex_rang=apex_rang, apex_zone=apex_zone, apex_hp_armor=apex_hp_armor,
                     path=path,
                     )


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")

style = ttk.Style()
style.configure('TCheckbutton', font=20)

prewatch_rf = Frame(window)
prewatch_rf.grid(column=2, row=0, rowspan=100)

lbl = Label(window, text="Введите путь к на видео:", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

lbl2 = Label(window, text=f"", font=("Arial Bold", 12), bg='lightgray', width=50)  # отображение пути к видео
lbl2.grid(column=0, row=1)

btn = ttk.Button(window, text="Обзор..", command=explore)
btn.grid(column=1, row=1)

btn2 = Button(window, text="Выбрать кадр", command=lambda: prewatch_frame(path))
btn2.grid(column=1, row=2)

btn2 = Button(window, text="Пререндр кадра", command=lambda: prerender_frame(path))
btn2.grid(column=1, row=3)

btn2 = Button(window, text="Рендер видео", command=lambda: render())
btn2.grid(column=1, row=4)

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

radio_var = IntVar()
rad1 = ttk.Radiobutton(radiobtns, text='CS2', value=1, command=drowframe_cs, variable=radio_var)
rad1.grid(column=0, row=0)

rad2 = ttk.Radiobutton(radiobtns, text='Apex', value=2, command=drowframe_apex, variable=radio_var)
rad2.grid(column=1, row=0, padx=20)

rad3 = ttk.Radiobutton(radiobtns, text='Any', value=3, command=drowframe_any, variable=radio_var)
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
    checkbox.grid(row=2 + len(checkboxes_entries_cs), column=0, sticky=W)
    entry.grid(row=2 + len(checkboxes_entries_cs), column=1, columnspan=2, sticky=E)


def add_checkbox_entry_apex():
    # Создаем новый Checkbox и Entry
    checkbox = ttk.Checkbutton(tab_apex, text="Checkbox")
    entry = Entry(tab_apex, width=38)
    entry.insert(0, 'Длина, Высота, Начиная с х, Начиная с y')

    # Добавляем Checkbox и Entry в список
    checkboxes_entries_apex.append((checkbox, entry))

    # Размещаем Checkbox и Entry на форме
    checkbox.grid(row=4 + len(checkboxes_entries_apex), column=0, sticky=W)
    entry.grid(row=4 + len(checkboxes_entries_apex), column=1, columnspan=2, sticky=E)


def add_checkbox_entry_any():
    # Создаем новый Checkbox и Entry
    checkbox = ttk.Checkbutton(tab_any, text="Checkbox")
    entry = Entry(tab_any, width=38)
    entry.insert(0, 'Длина, Высота, Начиная с х, Начиная с y')

    # Добавляем Checkbox и Entry в список
    checkboxes_entries_any.append((checkbox, entry))

    # Размещаем Checkbox и Entry на форме
    checkbox.grid(row=2 + len(checkboxes_entries_any), column=0, sticky=W)
    entry.grid(row=2 + len(checkboxes_entries_any), column=1, columnspan=2, sticky=E)


def print_values_cs():
    # Печатаем значения всех Checkbox и Entry
    for checkbox, entry in checkboxes_entries_cs:
        print(f"Checkbox: {checkbox.state()}, Entry: {entry.get()}")


def print_values_apex():
    # Печатаем значения всех Checkbox и Entry
    for checkbox, entry in checkboxes_entries_apex:
        print(f"Checkbox: {checkbox.state()}, Entry: {entry.get()}")


def print_values_any():
    # Печатаем значения всех Checkbox и Entry
    for checkbox, entry in checkboxes_entries_any:
        print(f"Checkbox: {checkbox.state()}, Entry: {entry.get()}")


chb_to916_cs = ttk.Checkbutton(tab_cs, text='to 9:16', padding=20, takefocus=0)
chb_to916_cs.grid(column=0, row=0)

chb_kills_cs = ttk.Checkbutton(tab_cs, text='kills', padding=20, takefocus=0)
chb_kills_cs.grid(column=1, row=0)

chb_players_cs = ttk.Checkbutton(tab_cs, text='players', padding=20, takefocus=0)
chb_players_cs.grid(column=2, row=0)

chb_radar_cs = ttk.Checkbutton(tab_cs, text='radar', padding=20, takefocus=0)
chb_radar_cs.grid(column=0, row=1)

chb_crop_cs = ttk.Checkbutton(tab_cs, text='crop', takefocus=0)
chb_crop_cs.grid(column=1, row=1, sticky=E)
ent_crop_cs = ttk.Entry(tab_cs)
ent_crop_cs.insert(0, '0.625')
# ent_crop.insert(0, '1200,1080,360,0')
ent_crop_cs.grid(column=2, row=1, sticky=W)

chb_webcam_cs = ttk.Checkbutton(tab_cs, text='webcam', padding=20, takefocus=0)
chb_webcam_cs.grid(column=0, row=2)

ttk.Button(tab_cs, text='Добавить crop', command=add_checkbox_entry_cs).grid(column=1, row=2)

print_button = Button(tab_cs, text="Печать значений", command=print_values_cs)
print_button.grid(column=2, row=2, pady=5)

chb_to916_apex = ttk.Checkbutton(tab_apex, text='to 9:16', padding=20, takefocus=0)
chb_to916_apex.grid(column=0, row=0)

chb_kills_apex = ttk.Checkbutton(tab_apex, text='kills, dmg', padding=20, takefocus=0)
chb_kills_apex.grid(column=0, row=3)

chb_rang_apex = ttk.Checkbutton(tab_apex, text='rang', padding=20, takefocus=0)
chb_rang_apex.grid(column=0, row=2)

chb_hp_apex = ttk.Checkbutton(tab_apex, text='hp', padding=20, takefocus=0)
chb_hp_apex.grid(column=2, row=1)

chb_hp_armor_apex = ttk.Checkbutton(tab_apex, text='hp with armor', padding=20, takefocus=0)
chb_hp_armor_apex.grid(column=2, row=2)

chb_radar_apex = ttk.Checkbutton(tab_apex, text='radar', padding=20, takefocus=0)
chb_radar_apex.grid(column=0, row=1)

chb_zone_apex = ttk.Checkbutton(tab_apex, text='zone', padding=20, takefocus=0)
chb_zone_apex.grid(column=1, row=1)

chb_crop_apex = ttk.Checkbutton(tab_apex, text='crop', takefocus=0)
chb_crop_apex.grid(column=1, row=0, sticky=E)
ent_crop_apex = ttk.Entry(tab_apex)
ent_crop_apex.insert(0, '0.53')
# ent_crop.insert(0, '1200,1080,360,0')
ent_crop_apex.grid(column=2, row=0, sticky=W)

chb_webcam_apex = ttk.Checkbutton(tab_apex, text='webcam', padding=20, takefocus=0)
chb_webcam_apex.grid(column=1, row=2)

ttk.Button(tab_apex, text='Добавить crop', command=add_checkbox_entry_apex).grid(column=0, row=4)

print_button = Button(tab_apex, text="Печать значений", command=print_values_apex)
print_button.grid(column=1, row=4, pady=5)

chb_to916_any = ttk.Checkbutton(tab_any, text='to 9:16', padding=20, takefocus=0)
chb_to916_any.grid(column=0, row=0)

chb_crop_any = ttk.Checkbutton(tab_any, text='crop', takefocus=0)
chb_crop_any.grid(column=1, row=0, sticky=E)
ent_crop_any = ttk.Entry(tab_any)
ent_crop_any.insert(0, '1,2')
# ent_crop.insert(0, '1200,1080,360,0')
ent_crop_any.grid(column=2, row=0, sticky=W)

chb_webcam_any = ttk.Checkbutton(tab_any, text='webcam', padding=20, takefocus=0)
chb_webcam_any.grid(column=0, row=1)

ttk.Button(tab_any, text='Добавить crop', command=add_checkbox_entry_any).grid(column=0, row=2)

print_button = Button(tab_any, text="Печать значений", command=print_values_any)
print_button.grid(column=1, row=1, pady=5)

# btn = ttk.Button(radiobtns, text="Обзор.", command= lambda: print(chb_players.state(), chb_kills.state()))
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
