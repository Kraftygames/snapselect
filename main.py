import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import os
import random
import images
import  selection_logic



def display_images(folder):
    pass


def main():
    my_images = images.get_images_from_folder(r'C:\Users\vince\OneDrive - Malayan Colleges Mindanao (A Mapúa School)\School\S.Y. 2022 - 2023\Student Council\MIECES\Bomber Jacket\hornet\step 2')
    selected = selection_logic.choose(lst=my_images, qty=2)

    for a in selected:
        print(a, end=', ')

    print()


if __name__ == '__main__':
    main()

