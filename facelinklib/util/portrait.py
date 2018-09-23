from PIL.Image import Image


class Portrait(Image):
    """
    Portraits are pictures of faces. Portrait images are created as a result
    of the face recognition module. The pictures of each face is then
    instantiated as a Portrait object.
    <br>
    There are no dangling unassigned as every Portrait must be of a Person.
    """

    def tostring(self, *args, **kw):
        pass

    def fromstring(self, *args, **kw):
        pass

    def offset(self, xoffset, yoffset=None):
        pass
