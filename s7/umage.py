#!/usr/bin/env python3

from PIL import Image  # Requires python-image-library (pillow)
import itertools


def load(filename):
    """ Given a filename that matches an image file,
    return a list of lists of tuples corresponding to the list of
    lines of pixels (R, G, B) of the image. """

    with Image.open(filename, 'r') as image:
        image = image.convert('RGB')
        content = list(image.getdata())
        size_x, size_y = image.size
        return [content[i:i + size_x] for i in range(0, len(content), size_x)]


def save(image, filename='new', extension='jpg'):
    """ Stores the given image into a file. The name
    of the file is set to <filename>.<extension> which is
    'new.jpg' by default. """

    size_x, size_y = len(image), len(image[0])
    new_image = Image.new('RGB', (size_y, size_x))
    new_image.putdata(list(itertools.chain.from_iterable(image)))
    new_image.save('%s.%s' % (filename, extension))
