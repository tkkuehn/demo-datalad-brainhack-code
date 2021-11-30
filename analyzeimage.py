"""Demo script that reads an image."""

import argparse

import nibabel as nib


parser = argparse.ArgumentParser()
parser.add_argument("img")
args = parser.parse_args()

img = nib.load(args.img)

print(img.shape)
