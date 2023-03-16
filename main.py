import tkinter as tk
import util
import cv2
from PIL import Image, ImageTk


def login():
    print("logged in")


def register():
    pass


def add_webcam(label):
    cap = cv2.VideoCapture(0)

    # _label = label
    #
    # frame = cap.read()
    # # recent_frame_arr = frame
    # _img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # most_recent_capture_pil = Image.fromarray(_img)
    #
    # imgtk = ImageTk.PhotoImage(image=most_recent_capture_pil)
    # _label.imgtk = imgtk
    # _label.configure(image=imgtk)

    # _label.after(20, )


#     process_webcam()
#
# def process_webcam(self):
#     ret, frame = cap.read()


mainWindow = tk.Tk()
mainWindow.geometry("1150x500")

loginButton = util.get_button(mainWindow, 'login', 'green', login)
loginButton.place(x=775, y=325)

registerButton = util.get_button(mainWindow, 'register', 'red', register)
registerButton.place(x=775, y=425)

mainWindow.minsize(1150, 550)
mainWindow.maxsize(1150, 550)

webcamLabel = util.get_img_label(mainWindow)
webcamLabel.place(x=10, y=0, width=700, height=500)
add_webcam(webcamLabel)

mainWindow.mainloop()
