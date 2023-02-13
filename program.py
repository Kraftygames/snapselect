import tkinter as tk
import images
from PIL import ImageTk, Image




def image_click(index):
    image_app.increase_score(image_app.selected_images[index])
    update_display()
    print(image_app.scores)
    pass


def update_display():
    for widget in root.winfo_children():
        widget.destroy()

    image_bin.clear()
    image_app.sample_images(2)

    left_image = image_app.get_image_object(index=0, resolution=(512, 512))
    image_bin.append(left_image)
    left_image_display = tk.Label(root, image=image_bin[0], width=512, height=512)
    left_image_display.grid(row=0, column=0)
    left_image_display.bind("<Button-1>", lambda e: image_click(0))

    # right image
    right_image = image_app.get_image_object(index=1, resolution=(512, 512))
    image_bin.append(right_image)
    right_image_display = tk.Label(root, image=image_bin[1], width=512, height=512)
    right_image_display.grid(row=0, column=1)
    right_image_display.bind("<Button-1>", lambda e: image_click(1))


root = tk.Tk()
image_app = images.ImageSelection(r'C:\Users\vince\OneDrive - Malayan Colleges Mindanao (A Mapúa School)\School\S.Y. 2022 - 2023\Student Council\MIECES\Bomber Jacket\hornet\step 2')
image_bin = []
update_display()
root.mainloop()

