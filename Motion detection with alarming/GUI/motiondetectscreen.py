import cv2
import tkinter as Tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import os
import subprocess
# scripts:
# from
class MotionDetection:
    def __init__(self, root):
        self.root = root
        self.root.title("Motion Detection mode")
        self.root.geometry("800x600")

        # Navigation bar
        self.nav_frame = Frame(self.root, bg="gray", width=200)
        self.nav_frame.pack(side=LEFT, fill=Y)
        
        Label(self.nav_frame, text="Navigation", bg="gray", fg="white", font=("Arial", 16)).pack(pady=10)
        
        nav_buttons = ["Home", "Motion detect mode", "face recognition mode" ,"Fire detection mode" ,"total Lockdown" ,"Freeze","Warning Alarms", "About", "Exit"]
        for btn in nav_buttons:
            Button(self.nav_frame, text=btn, width=15, bg="white", command=lambda b=btn: self.nav_action(b)).pack(pady=5)

        # Main content area
        self.main_frame = Frame(self.root, bg="white")
        self.main_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        
        self.camera_label = Label(self.main_frame)
        self.camera_label.pack(fill=BOTH, expand=True)
        
        self.cap = cv2.VideoCapture(0)  # Access the default camera
        self.running = True
        self.update_camera_feed()
        
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    # navigation:
    def nav_action(self, action):
        print(f"Navigation action: {action}")
        if action == "Exit":
            self.close_app()

    def run_program(self):
        self.my_button = Tk.Button(root, text="Motion detect mode", command=self.on_button_click)
        self.my_button.pack(pady=20)
    
    def on_button_click(self):
        print("motion detection mode activated")

    def update_camera_feed(self):
        if not self.running:
            return
        
        
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)
        
        self.root.after(10, self.update_camera_feed) 

    def close_app(self):
        self.running = False
        self.cap.release()
        self.root.destroy()

        


if __name__ == "__main__":
    root = Tk()
    app = MotionDetection(root)  
    root.mainloop()

