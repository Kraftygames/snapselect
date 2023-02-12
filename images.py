import os
import random

class ImageSelection:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.images = self.get_images_from_folder(self.folder_path)
        self.score_keeping_dict = self.convert_to_score_keeping_dict(self.images)
        self.selected_images = []



    def get_images_from_folder(self, folder_path):
        images = []
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                images.append(file_path)
        return images

    def convert_to_score_keeping_dict(self, input_list):
        score_keeping_dict = {}
        for item in input_list:
            if item not in score_keeping_dict:
                score_keeping_dict[item] = 0
        return score_keeping_dict

    def increase_score(self, key):
        if key in self.score_keeping_dict:
            self.score_keeping_dict[key] += 1
        else:
            self.score_keeping_dict[key] = 1

    def choose_images(self, qty):
        if len(self.images) < qty:
            self.selected_images = self.images
            return self.selected_images

        available = [elem for elem in self.images if elem not in self.selected_images]

        if len(available) >= qty:
            self.selected_images = random.sample(available, qty)
            return self.selected_images

        self.selected_images = random.sample(self.images, qty)
        return self.selected_images


def main():
    a = ImageSelection(r'C:\Users\vince\OneDrive\Pictures\memes')
    print(a.choose_images(2))


if __name__ == '__main__':
    main()
