import requests
import json
import pprint
import os
import filetype
import time
from io import BytesIO
from PIL import Image

# ログイン情報
MAIL = 'YOUR E-MAIL'
PASSWORD = 'YOUR PASSWORD'

# ダウンロード先
path = '/Users/YOUR PC NAME/Downloads/album'
os.makedirs(path, exist_ok=True)

# アルバム一覧情報を取ってきている
url = 'https://api.photozou.jp/rest/photo_album.json'
r = requests.get(url, auth=(MAIL, PASSWORD), verify=False)
json_data = r.json()
data = json_data['info']['album']

for i in data:
    # アルバム名のフォルダーを作成
    path = '/Users/YOUR PC NAME/Downloads/album/' + i['name']
    print(i['name'])
    os.makedirs(path, exist_ok=True)

    # フォルダーの中のファイルの数を数える
    files = os.listdir(path)
    count = len(files)

    # 写真数比較
    print(i['photo_num'], count)
    
    # ファイル数が写真の数と同じかそれ以上なら
    if count >= i['photo_num']:
        continue

    # アルバムの中の写真を取ってくる
    url = 'https://api.photozou.jp/rest/photo_album_photo.json'
    payload = {'album_id':i['album_id'], 'limit':'1000'}
    r = requests.get(url, params=payload, auth=(MAIL, PASSWORD), verify=False)
    json_data = r.json()
    data = json_data['info']['photo']

    # 何枚目かを数える
    num = 0

    # アルバム内の写真を保存する
    for j in data:
        time.sleep(0.5)
        # アルバムの写真のタイトル名
        print(j['photo_title'])
        # アルバム内の写真URL
        url = j['original_image_url']
        # 写真のイメージデータを取ってくる
        r = requests.get(url, auth=(MAIL, PASSWORD), verify=False)
        # 写真のデータ形式
        kind = filetype.guess(r.content)
        im = Image.open(BytesIO(r.content))
        # 何枚かを足す1して計算している
        num+=1
        # 写真の名前をつけて保存している
        im.save(path + '/' + j['photo_title'] + '_' + str(num) + '.' + kind.extension)
    # exit()