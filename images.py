import os
import random
from PIL import Image, ImageTk


def convert_to_score_keeping_dict(input_list):
    score_keeping_dict = {}
    for item in input_list:
        if item not in score_keeping_dict:
            score_keeping_dict[item] = 0
    return score_keeping_dict


def get_images_from_folder(folder_path):
    images = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            images.append(file_path)
    return images


class ImageSelection:
    def __init__(self, folder_path):
        self.folder = folder_path
        self.images = get_images_from_folder(self.folder)
        self.scores = convert_to_score_keeping_dict(self.images)
        self.selected_images = []

    def increase_score(self, key):
        if key in self.scores:
            self.scores[key] += 1
        else:
            self.scores[key] = 1

    def sample_images(self, qty):
        if len(self.images) < qty:
            self.selected_images = self.images
            return self.selected_images

        available = [elem for elem in self.images if elem not in self.selected_images]

        if len(available) >= qty:
            self.selected_images = random.sample(available, qty)
            return self.selected_images

        self.selected_images = random.sample(self.images, qty)
        return self.selected_images

    def get_image_object(self, index, resolution=None):
        original_image = Image.open(self.selected_images[index])

        if resolution is not None:
            original_image = original_image.resize(resolution, Image.Resampling.LANCZOS)

        return ImageTk.PhotoImage(original_image)


def main():
    a = ImageSelection(r'C:\Users\vince\OneDrive\Pictures\memes')
    print(a.images)
    print(a.scores)
    print(a.selected_images)
    a.sample_images(2)
    print(a.selected_images)
    a.increase_score(a.selected_images[0])
    print(a.scores)


if __name__ == '__main__':
    main()