import face_recognition
import time
import tqdm
from configuration import *
from detect_images import load_images_from_folder


def encode_pictures_of_me():
    # Get images of me
    pictures_of_me = load_images_from_folder(pictures_of_me_prepared)
    encodings_of_me = []
    print("Detecting face encodings of me in folder: ", pictures_of_me_prepared)

    for picture_of_me in tqdm.tqdm(pictures_of_me):
        time.sleep(0.01)

        # Create an encoding of my facial features that can be compared to other faces
        image_of_me = face_recognition.load_image_file(picture_of_me)

        # Cannot find a face
        if not len(face_recognition.face_encodings(image_of_me)) > 0:
            print("No faces found in the image: ", picture_of_me)

            # Take next image in folder
            continue

        # Add recognized face to my encodings
        encodings_of_me.append(face_recognition.face_encodings(image_of_me)[0])

    return encodings_of_me
