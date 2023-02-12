import tkinter as tk
from tkinter import PhotoImage
from random import choice
import images
import selection_logic
from PIL import ImageTk, Image


def update_images(root):
    for widget in root.winfo_children():
        widget.destroy()

    selected_images = function_b()

    # clear all widgets from the root window
    my_button1 = tk.Button(root, text="Click Me!", command=update_images)
    my_button1.pack()

    my_button2 = tk.Button(root, text="Click Me!", command=update_images)
    my_button2.pack()

    # create a list to store the image objects
    root.images = []

    # create a label for each image
    for image_path in selected_images:
        image_post = Image.open(image_path)
        resized_image = image_post.resize((512, 512), Image.Resampling.LANCZOS)
        converted_image = ImageTk.PhotoImage(resized_image)

        root.images.append(converted_image)

        my_label = tk.Label(root, image=converted_image, width=512, height=512)
        my_label.pack()
        my_label.bind("<Button-1>", on_image_click)


def score(lst_img):
    for imager in lst_img:


def on_image_click(root, event):
    # record which image was clicked
    clicked_image_path = event.widget.cget("image")
    print(clicked_image_path)

    new_images = function_b()
    update_images(root, new_images)


def main():
    root = tk.Tk()
    update_images(root)
    root.mainloop()


if __name__ == '__main__':
    main()
