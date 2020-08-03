import argparse
from PIL import Image

imgK = Image.open('kitten.jpeg')
imgP = Image.open('puppy.jpeg')

parser = argparse.ArgumentParser()
parser.add_argument("--kitten", help="Shows a cute kitten")
parser.add_argument("--puppy", help="Shows a cute puppy")
args=parser.parse_args()

if args.kitten:
    imgK.show()
if args.puppy:
    imgP.show()
