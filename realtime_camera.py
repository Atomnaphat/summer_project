import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os

class CameraViewer:
    def __init__(self, master, camera_index=0, folder_path="captured_images"):
        self.master = master
        self.folder_path = folder_path

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
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (640, 480))
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        self.video_label.configure(image=self.photo)
        self.video_label.image = self.photo
        self.video_label.after(10, self.show_frame)

    def capture_image(self):
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Create folder if it doesn't exist
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        # Save the captured frame
        image_path = os.path.join(self.folder_path, "captured_image.jpg")
        cv2.imwrite(image_path, frame)
        print("Image captured and saved.")

def main():
    root = tk.Tk()
    root.title("Camera Viewer")
    app = CameraViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
