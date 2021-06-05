# stash
hides a set of files into a binary image.  The generated binary image is encrypted using an 8-bit symmetric key supplied by the user.  You can add as many files as you want to the binary image.

## Usage

```bash
python3 stash.py test.img 81 myimg00.jpg myimg01.jpg
```

# unstash
extracts a set of files from a binary image.  It decrypts a binary image using an 8-bit symmetric key supplied by the user.

## Usage

```bash
python unstash.py test.img 81
```

# File formats supported

* jpeg
* gif
* png
* pdf

# TODO

Add file metadata to generated image to carve files with no trailer signatures...