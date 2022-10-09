import tkinter as tk
from PIL import Image, ImageTk, ImageFilter

# doggo = Image.open('doggo.jpg')
# stamp = Image.open('stamp.jpg').resize(doggo.size).convert(doggo.mode)
# blend = Image.blend(doggo, stamp, 0.5)
# print(stamp.mode)
# blend.show()

def watermark():
    stamp = Image.open('stamp.jpg').resize(window.imagesize).convert(window.imagemode)
    blended_image= Image.blend(window.current_image, stamp, 0.2)
    window.current_image=blended_image
    image2 = ImageTk.PhotoImage(blended_image)
    window.label.config(image = image2)
    # blended_image.show()
    window.current_image.show()
def blur():
    image3= window.current_image.filter(ImageFilter.BoxBlur(window.w.get()))
    window.current_image = image3
    blurred=ImageTk.PhotoImage(image3)
    window.label.config(image=blurred)
    window.current_image.show()
class Window:
    def __init__(self, master):
        # self.image=tk.PhotoImage(file = "doggo.jpg")


        self.pillow_image = Image.open("doggo.jpg") # 👉🏽 Read Image with pillow
        self.imagesize = self.pillow_image.size
        self.imagemode= self.pillow_image.mode
        self.current_image= self.pillow_image
        self.image = ImageTk.PhotoImage(self.pillow_image) # 👉🏽 Convert to compatible image with Tk
        self.label=tk.Label(master, image=self.image)
        # self.label = tk.Label(root, image=self.image)
        self.label.pack(padx=5, pady=5)
        self.label.grid(column=0, row=1, columnspan=4, padx=(100, 100), pady=(50, 20))

        self.button = tk.Button(text="Water Mark", pady=10,  bg='#7d8491', fg='black', bd='0', command=watermark, font=("Arial", 15, "italic"), highlightthickness=0)
        self.button.grid(padx=5,column=0, row=2, columnspan=2, pady=(10, 20))

        self.button2 = tk.Button(text="Blur", pady=10, bg='#7d8491', fg='black', bd='0', command=blur, font=("Arial", 15, "italic"), highlightthickness=0)
        self.button2.grid(padx=5, column=1, row=2, columnspan=2, pady=(10, 20))

        self.w = tk.Scale(master, from_=0, to=10, orient='horizontal')
        self.w.grid(padx=5, column=2, row=2, columnspan=2, pady=(5, 20))


# if(input("Mark stamp on image y/n?")) == 'y':
#     print('it is same')
root = tk.Tk()
root.configure(background= '#574b60')
window = Window(root)
root.mainloop()

