# Import custom dependencies
from configuration import *

# Import python dependencies
import os
import tqdm
import time
from shutil import copyfile
import face_recognition as face_recognition
# Load truncated images
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def detect_faces(face_encodings, image_paths):
    print("Parsing all images...")

    # Parse through all filenames
    for image_filename in tqdm.tqdm(image_paths):

        # Sleep a bit, problematic USB drivers, can be removed
        time.sleep(0.01)

        # Load this picture
        new_picture = face_recognition.load_image_file(image_filename)

        # Iterate through every face detected in the new picture
        for face_encoding in face_recognition.face_encodings(new_picture):

            # Iterate through every encoding of my face
            for encoding_of_me in face_encodings:

                # Run the algorithm of face comparison for the detected face, with 0.6 tolerance
                results = face_recognition.compare_faces([encoding_of_me], face_encoding, tolerance)

                # Save the image to a separate folder if there is a match
                if results[0]:
                    image_name = os.path.basename(image_filename)
                    copyfile(image_filename, match_found_location + image_name)

                    # One match was already found, take the next (applies to multiple face source images)
                    continue
