# stash
hides a set of files into a binary image.  The generated binary image is encrypted using an 8-bit symmetric key supplied by the user.  You can add as many files as you want to the binary image.

## Usage

```bash
python3 stash.py test.img 81 myimg00.jpg myimg01.jpg
```