from lib import magic
from pathlib import Path
from lib.file import File

class Extract:
    def __init__(self, fname, key):
        self.fname = fname
        self.key = bytes(int(key))[0]

    def extract(self):
        data = Path(self.fname).read_bytes()
        decryptedData = self.decrypt(data)

        for fileKey in magic.Magic.magicDict:
            print(f"Searching for file type [{fileKey}]")
            fileType = magic.Magic.magicDict[fileKey]["file_type"]
            startMagic = magic.Magic.magicDict[fileKey]["start_magic"]
            endMagic = magic.Magic.magicDict[fileKey]["end_magic"]

            fileCount = 0

            foundFile = self.findFile(0, decryptedData, startMagic, endMagic)
        
            while foundFile != None:
                print(f"Discovered a file of type [{fileType}]")
                self.dumpFile(foundFile.getData(), str(fileCount), fileType)
                foundFile = self.findFile(foundFile.getIndex(), decryptedData, startMagic, endMagic)
                fileCount = fileCount + 1



    def findFile(self, index, buffer, startMagic, endMagic):
        sz = len(buffer)
        startMagicSz = len(startMagic)
        endMagicSz = len(endMagic)
        foundFile = None
        fileCount = 0

        while index < sz:
            b = buffer[index]

            if startMagic[0] == b:
                i = 0
                found = True
                #print("Found first byte of magic!")

                while i < startMagicSz and found:
                    
                    if buffer[index] != startMagic[i]:
                        found = False

                    i=i+1
                    index = index+1

                if found:
                    f = self.extractFile(index, buffer, startMagic, endMagic)

                    if f != None:
                        foundFile = f
                        break                    


            index = index+1
        
        return foundFile

    
    def extractFile(self, index, buffer, startMagic, endMagic):
        fileData = bytearray(startMagic)
        endMagicSz = len(endMagic)

        while index < len(buffer):
            if buffer[index] == endMagic[0]:
                i = 0
                found = True

                while i < endMagicSz and found and index < len(buffer):
                    offset = index
                    if buffer[offset+i] != endMagic[i]:
                        found = False

                    i=i+1

                if found and i == endMagicSz:
                    fileData.extend(endMagic)
                    f = File(fileData, index)
                    return f

            fileData.append(buffer[index])
            index=index+1

        return None

    
    def decrypt(self, buffer):
        i = 0
        sz = len(buffer)
        decryptedBuffer = bytearray()

        while i < sz:
            b = buffer[i]
            d = b ^ self.key
            decryptedBuffer.append(d)
            i = i+1

        return decryptedBuffer

    def dumpFile(self, fData, fname, ftype):
        fout = fname + "." + ftype
        fh = open(fout, "wb")
        fh.write(fData)
        fh.close()