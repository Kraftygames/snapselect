# Image Selection GUI

A GUI application to select images and display the best image after multiple selections. 

## Features
- Select a folder containing images
- Display two random images from the folder
- Select the best image by clicking on it
- The selection process continues until all images have been evaluated or a certain number of evaluations have been made
- The image with the most selections is displayed at the end

## Requirements
- Python 3
- tkinter
- PIL (Python Imaging Library)

## Usage
1. Clone the repository or download the ZIP file
2. Install the required libraries
3. Run the program using `python main.py`
4. Press the `Browse` button and select a folder containing images
5. Select the best image by clicking on it. The selection process continues until all images have been evaluated or a certain number of evaluations have been made.
6. The image with the most selections is displayed at the end.

## Files
- main.py: The main Python file that contains the GUI code
- images.py: A module containing the `ImageSelection` class that handles the image selection process
- images/: A directory containing sample images used for testing

## License
This project is licensed under the MIT License.
