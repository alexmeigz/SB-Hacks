import os
from rgb import *
from google.cloud import vision
import io

GOOGLE_APPLICATION_CREDENTIALS = "/Users/alex/Desktop/app_credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

def detect_properties(path):
    """Detects image properties in the file."""

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print('Properties:')

    for color in props.dominant_colors.colors:
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))


    dominant = determineDominant(props.dominant_colors.colors)
    return dominant
        
def determineDominant(colors):
    dominant = None
    fraction = 0
    for color in colors:
        if fraction < color.pixel_fraction:
            fraction = color.pixel_fraction
            dominant = RGB(color.color.red, color.color.green, color.color.blue)
    print(dominant)
    return dominant

