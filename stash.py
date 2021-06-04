from sys import argv
from lib.imggen import ImgGen

def main(argv):
    if len(argv) < 3:
        print("python3 stash.py <image name> <file1> ... <fileN>")
        print("image name - the name of the binary image you want to create.")
        print("file1 ... fileN - a set of files you want embedded into the binary image.")
        return

    sz = len(argv)
    imgGen = ImgGen(argv[1], argv[2:sz])
    imgGen.generate()

main(argv)