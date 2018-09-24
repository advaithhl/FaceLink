from PIL.Image import Image


class Photo(Image):
    """
    Photo is the representation of a single photo given to be processed.
    Every photo given as input is instantiated into a Photo object, which is
    passed to other functions to extract faces.
    """

    def __init__(self):
        super().__init__()

    def tostring(self, *args, **kw):
        pass

    def fromstring(self, *args, **kw):
        pass

    def offset(self, xoffset, yoffset=None):
        pass
