import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class CameraViewer:
    def __init__(self, master, camera_index=1):
        self.master = master

        self.capture_button = tk.Button(master, text="Capture", command=self.capture_image)
        self.capture_button.pack()

        self.video_label = tk.Label(master)
        self.video_label.pack()

        # Connect to camera
        self.capture = cv2.VideoCapture(camera_index)

        # Start video streaming
        self.show_frame()

    def show_frame(self):
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
        frame = cv2.resize(frame, (640, 480))
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        self.video_label.configure(image=self.photo)
        self.video_label.image = self.photo
        self.video_label.after(10, self.show_frame)

    def capture_image(self):
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Get save file path
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if file_path:
            cv2.imwrite(file_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))  # Convert back to BGR before saving
            print("Image captured and saved.")

def main():
    root = tk.Tk()
    root.title("Camera Viewer")
    app = CameraViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
