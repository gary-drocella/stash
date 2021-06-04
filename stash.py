
/**
 * stash is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * stash is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with stash.  If not, see <https://www.gnu.org/licenses/>.
 */
 
from sys import argv
from lib.imggen import ImgGen

def main(argv):
    if len(argv) < 4:
        print("python3 stash.py <image name> <key> <file1> ... <fileN>")
        print("image name - the name of the binary image you want to create.")
        print("key - an eight bit symmetric key used to encrypt the image.")
        print("file1 ... fileN - a set of files you want embedded into the binary image.")
        return

    sz = len(argv)
    imgGen = ImgGen(argv[1], argv[2], argv[3:sz])
    imgGen.generate()

main(argv)