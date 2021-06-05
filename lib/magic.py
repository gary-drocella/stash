class Magic:
    magicDict = {
        "jpeg" : {
            "file_type" : "jpeg",
            "start_magic" : bytearray(b"\xff\xd8\xff\xe0"),
            "end_magic" : bytearray(b"\xff\xd9")
        },
        "png" : {
            "file_type" : "png",
            "start_magic" : bytearray(b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"),
            "end_magic" : bytearray(b"\x49\x45\x4e\x44\xae\x42\x60\x82")
        },
        "pdf type 1" : {
            "file_type" : "pdf",
            "start_magic" : bytearray(b"\x25\x50\x44\x46"),
            "end_magic" : bytearray(b"\x0a\x25\x25\x45\x4f\x46")
        },
        "pdf type 2" : {
            "file_type" : "pdf",
            "start_magic" : bytearray(b"\x25\x50\x44\x46"),
            "end_magic" : bytearray(b"\x0a\x25\x25\x45\x4f\x46\x0a")
        },
        "pdf type 3" : {
            "file_type" : "pdf",
            "start_magic" : bytearray(b"\x25\x50\x44\x46"),
            "end_magic" : bytearray(b"\x0d\x0a\x25\x25\x45\x4f\x46\x0d\x0a")
        },
        "pdf type 4" : {
            "file_type" : "pdf",
            "start_magic" : bytearray(b"\x25\x50\x44\x46"),
            "end_magic" : bytearray(b"\x0d\x25\x25\x45\x4f\x46\x0d")
        },
        "gif type 1" : {
            "file_type" : "gif",
            "start_magic" : bytearray(b"\x47\x49\x46\x38\x37\x61"),
            "end_magic" : bytearray(b"\x00\x3b")
        },
        "gif type 2" : {
            "file_type" : "gif",
            "start_magic" : bytearray(b"\x47\x49\x46\x38\x39\x61"),
            "end_magic" : bytearray(b"\x00\x3b")
        }
    }