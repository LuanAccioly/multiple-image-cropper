import os
import numpy as np
import cv2
from matplotlib import pyplot as plt


def read_yolo_coordinates(file_path, img_width, img_height):
    coordinates = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            class_index, x_center, y_center, width, height = map(float, line.split())
            x_min = int((x_center - width / 2) * img_width)
            y_min = int((y_center - height / 2) * img_height)
            x_max = int((x_center + width / 2) * img_width)
            y_max = int((y_center + height / 2) * img_height)
            coordinates.append((x_min, y_min, x_max, y_max))
    return coordinates


def crop_questions(image_name):
    cropped_questions_path = "content/cropped_questions/"
    full_images_path = "content/full_images/"
    full_images_notation_path = "content/yolo_coordinates/questions/"

    image_path = full_images_path + image_name + ".jpg"
    yolo_coordinates_path = full_images_notation_path + image_name + ".txt"

    images = []
    image = cv2.imread(image_path)
    image
    img_height, img_width, _ = image.shape
    yolo_coordinates = read_yolo_coordinates(
        yolo_coordinates_path, img_width, img_height
    )

    for i, (x_min, y_min, x_max, y_max) in enumerate(yolo_coordinates):
        cropped_img = image[y_min:y_max, x_min:x_max]
        images.append(cropped_img)
        cv2.imwrite(f"{cropped_questions_path}{image_name}_{i+1}.jpg", cropped_img)
    return images


def remove_extension(files):
    file_names = []

    for file in files:
        file_name = file.split(".")[0]
        file_names.append(file_name)

    return file_names


if __name__ == "__main__":
    full_images_path = remove_extension(
        [file for file in os.listdir("content/full_images/") if ".gitkeep" not in file]
    )

    for image_name in full_images_path:
        crop_questions(image_name)
