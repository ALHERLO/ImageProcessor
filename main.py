import tkinter as tk
from PIL import Image, ImageTk

# doggo = Image.open('doggo.jpg')
# stamp = Image.open('stamp.jpg').resize(doggo.size).convert(doggo.mode)
# blend = Image.blend(doggo, stamp, 0.5)
# print(stamp.mode)
# blend.show()

class Window:
    def __init__(self, master):
        # self.image=tk.PhotoImage(file = "doggo.jpg")
        self.pillow_image = Image.open("doggo2.jpg") # 👉🏽 Read Image with pillow
        self.image = ImageTk.PhotoImage(self.pillow_image) # 👉🏽 Convert to compatible image with Tk
        self.label=tk.Label(master, image =self.image)
        self.label.pack(padx=5, pady=5)


if(input("Mark stamp on image y/n?")) == 'y':
    print('it is same')
root = tk.Tk()
window = Window(root)
root.mainloop()

