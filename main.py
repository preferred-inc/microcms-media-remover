import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_ENDPOINT = os.environ['API_ENDPOINT']
API_KEY = os.environ['API_KEY']

HEADERS = {
    'X-MICROCMS-API-KEY': API_KEY
}

def get_media_list():
    url = f"{API_ENDPOINT}"
    params = {
        'imageOnly': 'true',  # 画像のみ取得するパラメータ
        'limit': 100  # 最大100件取得
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def delete_media(media_url):
    delete_url = f"{API_ENDPOINT}"
    params = {
        'url': media_url
    }
    response = requests.delete(delete_url, headers=HEADERS, params=params)
    response.raise_for_status()
    print(f"Deleted media with URL: {media_url}")

def main():
    media_data = get_media_list()
    
    for media in media_data['media']:
        media_url = media['url']  # メディアのURLを取得
        delete_media(media_url)

if __name__ == '__main__':
    main()