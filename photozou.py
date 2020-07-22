import requests
import json
import pprint
import os
import filetype
from io import BytesIO
from PIL import Image

path = '/Users/taniteiko/Downloads/album'
os.makedirs(path, exist_ok=True)

url = 'https://api.photozou.jp/rest/photo_album.json'

r = requests.get(url, auth=('51830002.cj@gmail.com', 'kureteyaru'), verify=False)

json_data = r.json()
data = json_data['info']['album']

for i in data:
    path = '/Users/taniteiko/Downloads/album/' + i['name']
    print(i['name'])
    print(i['photo_num'])
    os.makedirs(path, exist_ok=True)

    url = 'https://api.photozou.jp/rest/photo_album_photo.json'
    payload = {'album_id':i['album_id'], 'limit':'1000'}

    r = requests.get(url, params=payload, auth=('51830002.cj@gmail.com', 'kureteyaru'), verify=False)

    json_data = r.json()
    data = json_data['info']['photo']
    num = 0
    for j in data:
        print(j['photo_title'])
        url = j['original_image_url']
        r = requests.get(url, auth=('51830002.cj@gmail.com', 'kureteyaru'), verify=False)
        kind = filetype.guess(r.content)
        im = Image.open(BytesIO(r.content))
        num+=1
        im.save(path + '/' + j['photo_title'] + '_' + str(num) + '.' + kind.extension)
    # exit()