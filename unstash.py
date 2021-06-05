
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
 
from sys import argv
from lib.extract import Extract

def main(argv):
    if len(argv) < 3:
        print("python3 unstash.py <image name> <key>")
        print("image name - the name of the binary image you want unstash files from")
        print("key - an eight bit symmetric key used to decrypt the image.")
        return

    extractor = Extract(argv[1], argv[2])
    extractor.extract()

main(argv)