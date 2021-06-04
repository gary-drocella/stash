# stash is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# stash is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with stash.  If not, see <https://www.gnu.org/licenses/>.
 
from random import randint
from pathlib import Path
import os

class ImgGen:
    def __init__(self, fname, key, files):
        self.fname = fname
        self.files = files
        self.key = bytes(int(key))[0]

    def generate(self):
        findex = 0
        fohandle = open(self.fname, "wb")
        fohandle.truncate()

        while findex < len(self.files):
            rblock = self.getRandBlock()
            encRBlock = self.encrypt(rblock)
            fdata = Path(self.files[findex]).read_bytes()
            encFData = self.encrypt(fdata)

            fohandle.write(encRBlock)
            fohandle.write(encFData)

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

    def encrypt(self, data):
        encData = bytearray()

        for datum in data:
            encDatum = datum ^ self.key
            encData.append(encDatum)

        return encData

