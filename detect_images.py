# Import
import glob

import cv2
import tqdm


def load_images_from_folder(folder):
    print("Loading images in folder: ", folder)
    images = []
    for filename in tqdm.tqdm(glob.iglob(folder + '**/*', recursive=True)):

        # Attempt to read image
        image = cv2.imread(filename)

        # If it is an valid image file
        if image is not None:
            images.append(filename)

    return images
