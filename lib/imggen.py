from random import randint
from pathlib import Path
import os

class ImgGen:
    def __init__(self, fname, files):
        self.fname = fname
        self.files = files

    def generate(self):
        findex = 0
        fohandle = open(self.fname, "wb")
        fohandle.truncate()
        
        while findex < len(self.files):
            rblock = self.getRandBlock()
            fdata = Path(self.files[findex]).read_bytes()
            fohandle.write(rblock)
            fohandle.write(fdata)

            findex=findex+1

        fohandle.write(self.getRandBlock())
        fohandle.close()

    def getRandKbs(self):
        minKbs = 0
        maxKbs = 2
        return randint(minKbs, maxKbs)

    def getRandBlock(self):
        size = 1024*2**self.getRandKbs()
        randData = os.urandom(size)
        return randData
