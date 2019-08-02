# Import custom files
from get_face import *
from detect_faces import detect_faces

# Create an encoding array of images in "face_me"
encodings_of_me = encode_pictures_of_me()

# Get all filenames of valid images in "face_dataset"
image_filenames = load_images_from_folder(pictures_of_everybody)

# Recognize faces and move the associated images to "face_results"
detect_faces(encodings_of_me, image_filenames)

# Finished processing
print("DONE")
