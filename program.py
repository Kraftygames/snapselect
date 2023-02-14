import tkinter as tk
import images
from PIL import ImageTk, Image
from tkinter import filedialog


def image_click(index):
    image_app.increase_score(image_app.selected_images[index])
    update_image_display()
    print(image_app.scores)
    return


def update_image_display():
    for widget in photo_wrapper.winfo_children():
        widget.destroy()

    image_bin.clear()
    image_app.sample_images(2)

    left_image = image_app.get_image_object(index=0, resolution=(512, 512))
    image_bin.append(left_image)
    left_image_display = tk.Label(photo_wrapper, image=image_bin[0], width=512, height=512)
    left_image_display.grid(row=0, column=0)
    left_image_display.bind("<Button-1>", lambda e: image_click(0))

    # right image
    right_image = image_app.get_image_object(index=1, resolution=(512, 512))
    image_bin.append(right_image)
    right_image_display = tk.Label(photo_wrapper, image=image_bin[1], width=512, height=512)
    right_image_display.grid(row=0, column=1)
    right_image_display.bind("<Button-1>", lambda e: image_click(1))






root = tk.Tk()


title = tk.Label(root, text="This is the title")
title.pack()



def file_function():
    global image_app
    file_path = '{}'.format(tk.filedialog.askdirectory(title='Browse'))
    image_app = images.ImageSelection(file_path)
    update_image_display()
    return image_app


directory_button = tk.Button(root, text='Browse...', command=lambda :file_function())

directory_button.pack()


photo_wrapper = tk.Frame(root)
photo_wrapper.pack()
image_bin = []
#update_image_display()
root.mainloop()

