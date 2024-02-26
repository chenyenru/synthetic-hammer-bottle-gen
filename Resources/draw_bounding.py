import cv2
import os
import numpy as np


def draw_bounding_box(image_path, bbox_path, output_folder):
    # Read image
    img = cv2.imread(image_path)
    dh, dw, _ = img.shape

    # Read bounding box coordinates from text file
    with open(bbox_path, "r") as file:
        # class_id, x, y, w, h = map(float, file.readLine().split())
        _, x, y, w, h = map(float, file.readline().split())

    # Draw bounding box on image
    l = int((x - w / 2) * dw)
    r = int((x + w / 2) * dw)
    t = int((y - h / 2) * dh)
    b = int((y + h / 2) * dh)
    cv2.rectangle(img, (l, t), (r, b), (0, 255, 0), 2)

    # Save the result to the output folder
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(output_path, img)

    return img


def process_images(image_folder, bbox_folder, output_folder, target_size=(640, 480)):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        # raise FileNotFoundError("Output Folder doesn't exist")
        os.makedirs(output_folder)

    images = []

    image_files = [
        f
        for f in sorted(os.listdir(image_folder))
        if f.endswith(("_1.jpg", "_1.jpeg", "_1.png"))
    ]
    # Loop through each image in the image folder
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)

        # Check if corresponding bounding box file exists
        bbox_file = os.path.join(
            bbox_folder, image_file.replace(os.path.splitext(image_file)[1], ".txt")
        )
        if os.path.exists(bbox_file):
            img_with_bbox = draw_bounding_box(image_path, bbox_file, output_folder)
            img_with_bbox = cv2.resize(img_with_bbox, target_size)
            images.append(img_with_bbox)
    return images


def save_as_video(images, video_path, fps=10):
    h, w, _ = images[0].shape
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(video_path, fourcc, fps, (w, h))

    for img in images:
        video_writer.write(img)

    video_writer.release()


if __name__ == "__main__":
    # Provide paths to image folder, bounding box folder, and output folder
    image_folder = "DATA/Images"
    bbox_folder = "DATA/Labels"
    output_folder = "DATA/Labeled_Images"
    video_path = "result.mp4"

    # Process images and save the results
    images = process_images(image_folder, bbox_folder, output_folder)

    save_as_video(images, video_path)
