#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_imageinfo.py

    MediaWiki Action API Code Samples
    Demo of `Imageinfo` module: Get information about an image file.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:Billy_Tipton.jpg"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
