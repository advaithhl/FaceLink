from pathlib import Path

from PIL import Image

from facelinklib import RESULTS
from facelinklib.util.photo import Photo


def get_photos(path: Path):
    """
    Yield pictures as Photo objects in a directory.

    :param path: Directory containing the pictures
    :return: generator object which yields Photo(s)
    """

    return (Photo(x) for x in path.iterdir() if x.is_file())


def detect_faces(photo: Photo):
    """
    Detect faces of everyone present in a picture represented as Photo object.
    Faces are detected using the face_recognition module, and outer boundaries
    of the faces are stored as coordinates. The coordinates which are stored
    in a list in the NumPy array interface format and returned.

    :param photo: Photo object from which the faces are to be found
    :return: list of images formatted in array interface
    """
    import face_recognition as fr
    img = fr.load_image_file(photo.path)
    print('Loaded', photo.path)
    face_locations = fr.face_locations(img)
    print('find_faces done')

    face_images = []
    for face_location in face_locations:
        top, right, bottom, left = face_location

        face_image = img[top:bottom, left:right]
        face_images.append(face_image)

    return face_images


def store_faces(photo: Photo, face_images):
    """
    Crop all pictures of all faces from the argument according to the
    coordinates detected by detect_faces method. Every such picture is stored
    in folders whose names are the same as the photo from which the face was
    detected.

    For example, if Alice's face was detected from Photo1.jpg, the portion of
    Photo1.jpg pertaining to Alice's face is cropped and saved as
    unknown<n>.jpg in a folder named Photo1. Every such folder is kept inside
    a larger folder named 'results'.

    :param photo: Photo which has the faces we are storing
    :param face_images: list of images formatted in array interface
    """

    if not RESULTS.exists():
        RESULTS.mkdir()
    img_folder = RESULTS.joinpath(photo.filename)
    img_folder.mkdir()

    for (sno, face_image) in enumerate(face_images):
        pil_image = Image.fromarray(face_image)
        face_img_name = img_folder.joinpath('unknown{}.jpg'.format(str(sno)))
        pil_image.save(face_img_name)
