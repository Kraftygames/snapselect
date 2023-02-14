import tkinter as tk
import images
from tkinter import filedialog


def image_click(index):
    if index is None:
        update_image_display()
        return

    image_app.increase_score(image_app.selected_images[index])

    step_number = step[0]

    if step_number >= 2 * len(image_app.images):
        final_display()
    else:
        update_image_display()

    step.clear()
    step.append(step_number + 1)
    return


def get_max_key(dictionary):
    max_key = None
    max_value = float('-inf')
    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


def final_display():
    for widget in photo_wrapper.winfo_children():
        widget.destroy()

    best_image = get_max_key(image_app.scores)

    image_bin.clear()
    final = image_app.get_image_object(path=best_image, resolution=(512, 512))
    image_bin.append(final)
    left_image_display = tk.Label(photo_wrapper, image=image_bin[0], width=512, height=512)
    left_image_display.pack()

    # path_text = tk.Entry(photo_wrapper)
    # path_text.insert(tk.INSERT, best_image)
    # path_text.pack()

    score_display = tk.Label(photo_wrapper, text=f"Score: {image_app.scores.get(best_image)}")
    score_display.pack()

    root.unbind_all("<Left>")
    root.unbind_all("<Right>")
    root.unbind_all("<Down>")


def update_image_display():
    for widget in photo_wrapper.winfo_children():
        widget.destroy()

    image_bin.clear()
    image_app.sample_images(2)

    left_image = image_app.get_image_object_from_selection(index=0, resolution=(512, 512))
    image_bin.append(left_image)
    left_image_display = tk.Label(photo_wrapper, image=image_bin[0], width=512, height=512)
    left_image_display.grid(row=0, column=0)
    left_image_display.bind("<Button-1>", lambda e: image_click(0))

    # right image
    right_image = image_app.get_image_object_from_selection(index=1, resolution=(512, 512))
    image_bin.append(right_image)
    right_image_display = tk.Label(photo_wrapper, image=image_bin[1], width=512, height=512)
    right_image_display.grid(row=0, column=1)
    right_image_display.bind("<Button-1>", lambda e: image_click(1))

    root.bind("<Left>", lambda event: image_click(0))
    root.bind("<Right>", lambda event: image_click(1))
    root.bind("<Down>", lambda event: image_click(None))


def file_function():
    global step
    global image_app
    file_path = '{}'.format(tk.filedialog.askdirectory(title='Browse'))
    image_app = images.ImageSelection(file_path)
    update_image_display()
    step = [0]
    return


root = tk.Tk()

directory_button = tk.Button(root, text='Browse...', command=lambda: file_function())
directory_button.pack()

photo_wrapper = tk.Frame(root)
photo_wrapper.pack()
image_bin = []
root.mainloop()
