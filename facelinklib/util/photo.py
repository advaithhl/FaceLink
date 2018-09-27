from pathlib import Path


class Photo:
    """
    Photo is the representation of a single photo given to be processed.
    Every photo given as input is instantiated into a Photo object, which is
    passed to other functions to extract faces.
    """

    def __init__(self, path: Path):
        self.path = path

    @property
    def filename(self):
        return self.path.name.split('.')[0]

    @property
    def extension(self):
        return self.path.suffix

    def tostring(self, *args, **kw):
        raise NotImplementedError("tostring() has been removed. "
                                  "Please call tobytes() instead.")

    def fromstring(self, *args, **kw):
        raise NotImplementedError("fromstring() has been removed. "
                                  "Please call frombytes() instead.")

    def offset(self, xoffset, yoffset=None):
        pass
