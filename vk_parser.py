import csv
import requests


def take_1000_posts():
    token = ''
    version = '5.95'
    domain = 'fit4life_official'
    count = 100
    offset = 0
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )

        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(data):
    with open('fit4life.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass

            a_pen.writerow((post['likes']['count'], post['text'], img_url))


all_posts = take_1000_posts()
file_writer(all_posts)