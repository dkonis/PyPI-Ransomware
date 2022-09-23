# PyPI-Ransomware
## PyPI Ransomware POC (For Educational Purposes Only).
[![Python 3.10.4](https://img.shields.io/badge/Python-3.10.4-yellow.svg)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

## About
PyPI-Ransomware is a ransomware POC that runs from the setup.py script of a package I created.

If installed by mistake, please go to the Decrypt section in Usage.

PyPI POC url: https://pypi.org/project/WARNING-PyPI-Ransomeware/

Note: the POC is by no means a good ransomware, it only utilizes symmetric encryption with an hardcoded key.

## Requirements
The POC requires [Python3](https://www.python.org/) and pip to use.

## Usage
### Encrypt:
WARNING: The POC will encrypt your files, use at your own risk.
```bash
pip install WARNING-PyPI-Ransomeware
```
### Decrypt:
To decrypt your files use the decrypt.py script with the KEY file in the Decrypter directory on the user's desktop:
```bash
python3 decrypt.py
```

## License
Distributed under the MIT License. See LICENSE.txt for more information.