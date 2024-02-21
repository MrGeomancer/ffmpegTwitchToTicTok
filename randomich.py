import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

class VideoPlayer:
    def __init__(self, root, video_path):
        self.root = root
        self.root.title("Video Player")

        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.num_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

        self.slider = ttk.Scale(root, from_=0, to=self.num_frames - 1,
                                orient="horizontal", command=self.on_slider_move)
        self.slider.pack(fill="x")

        self.frame_width = int(self.cap.get(3))
        self.frame_height = int(self.cap.get(4))

        self.canvas = tk.Canvas(root, width=self.frame_width, height=self.frame_height)
        self.canvas.pack()

        self.current_frame = 0
        self.update_canvas()

    def on_slider_move(self, value):
        try:
            frame_number = int(float(value))
            self.current_frame = frame_number
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            self.update_canvas()
        except ValueError:
            pass

    def update_canvas(self):
        ret, frame = self.cap.read()
        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image=image)

            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    video_path = "outputt_radar56.mp4"  # Замените на полный путь к вашему видеофайлу
    player = VideoPlayer(root, video_path)
    root.mainloop()
