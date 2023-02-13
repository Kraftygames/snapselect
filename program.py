import tkinter as tk
import images
from PIL import ImageTk, Image


def click_application(root):

    for widget in root.winfo_children():
        widget.destroy()

    root.images_app = images.ImageSelection(r'C:\Users\vince\OneDrive - Malayan Colleges Mindanao (A Mapúa School)\School\S.Y. 2022 - 2023\Student Council\MIECES\Bomber Jacket\hornet\step 2')
    root.images_app.sample_images(2)

    # clear all widgets from the root window
    # create a list to store the image objects
    root.image_bin = []


    #left image
    left_image = root.images_app.get_image_object(index=0, resolution=(512, 512))
    root.image_bin.append(left_image)
    left_image_display = tk.Label(root, image=root.image_bin[0], width=512, height=512)
    left_image_display.grid(row=0, column=0)
    left_image_display.bind("<Button-1>", lambda e: score_it(root, 0))


    #right image
    right_image = root.images_app.get_image_object(index=1, resolution=(512,512))
    root.image_bin.append(right_image)
    right_image_display = tk.Label(root, image=root.image_bin[1], width=512, height=512)
    right_image_display.grid(row=0, column=1)
    right_image_display.bind("<Button-1>", lambda e: score_it(root, 1))




def score_it(root, index):
    root.images_app.increase_score(root.images_app.selected_images[index])
    click_application(root)


def main():
    root = tk.Tk()
    click_application(root)
    print(root.images_app.scores)
    root.mainloop()


if __name__ == '__main__':
    main()
