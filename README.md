# Photozou all download by APIREST

"Photozou all download by APIREST” is a script that accesses the Photozou API and downloads all the photos in your account by dividing them into folders by album.

# DEMO

I made it because Photozou didn't have the ability to download all the photos in your account.

![demo](https://user-images.githubusercontent.com/28686632/88244706-95199600-cccf-11ea-9904-4919ad95823f.gif)

I spent a lot of time and effort getting the photos in the album, but now I can use my time for something else.

# Features

Below 8 I used this module.

```python
import requests
import json
import pprint
import os
import filetype
import time
from io import BytesIO
from PIL import Image
```
I retrieved the data in the API with requests.
I read the data retrieved by json.
The filetype was used to determine if the photo was in jpeg, png, or another file format.
Reduced the possibility of continuous access with time.

# Requirement

* Python 3.7
* requests 2.24.0
* opencv-python 4.3.0.36
* pillow 7.2.0
* filetype 1.0.7

Environments under [Pipenv for Mac] is tested.

```bash
pip install pipenv 
mkdir myProjcet
cd myProjcet
pipenv install --python=3.7
pipenv shell
```

# Installation

Install Pyxel with pip command.

```bash
pipenv install requests
pipenv install pprint
pipenv install opencv-python
pipenv install filetype
```

# Usage

Please create python code named "photozou.py".

```bash
git clone https://github.com/hoge/~
cd examples
python photozou.py
```

# Note

I don't test environments under Linux and Windows.

# Author

* Bern
* Twitter : https://twitter.com/bern673

# License

For photozou users who are in trouble somewhere in the world.

Thank you!
