full_files = [
    "info.txt",
    "image.png",
    "script.c",
    "image2.jpg",
    "info.3.txt"
]

for file in full_files:
    name = ".".join(file.split(".")[0:-1])
    print(name)
