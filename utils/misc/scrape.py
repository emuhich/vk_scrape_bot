import asyncio
import json
import os
import time

import requests
import vk_api
from aiogram import types

from dotenv import load_dotenv

from loader import dp

load_dotenv()

VK_BOT_TOKEN = str(os.getenv("VK_BOT_TOKEN"))


async def start(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        print('Время пришло!')
        with open("json/group.json", "r") as f:
            jsn: dict = json.load(f)
        group_list = [*jsn]
        for group_name in group_list:
            unique_id, owner_id = await get_unique_id(group_name, jsn)
            await get_post_content(unique_id, jsn, owner_id, group_name)
            list_id = jsn[group_name]['id']
            for id in unique_id:
                list_id.append(id)
            jsn[group_name].update({'id': list(set(list_id))})
            with open("json/group.json", 'w') as f:
                json.dump(jsn, f)


async def get_unique_id(group, jsn):
    vk_session = vk_api.VkApi(token=VK_BOT_TOKEN)
    vk = vk_session.get_api()
    a = vk.wall.get(count=30, domain=group)
    list_id = [i['id'] for i in a['items']]
    previous_id = jsn[group]['id']
    owner_id = a['items'][0]['owner_id']
    unique_id = []
    for id in list_id:
        if id not in previous_id:
            unique_id.append(id)
    return unique_id, owner_id


async def get_post_content(unique_id, jsn, owner_id, group_name):
    vk_session = vk_api.VkApi(token=VK_BOT_TOKEN)
    vk = vk_session.get_api()
    for id in unique_id:
        a = vk.wall.getById(posts=f'{owner_id}_{id}')
        post_id = a[0]["id"]
        if "attachments" in a[0]:
            post = a[0]['attachments']
            if post[0]['type'] == 'video':
                video_access_key = post[0]["video"]["access_key"]
                video_post_id = post[0]["video"]["id"]
                video_owner_id = post[0]["video"]["owner_id"]
                video = vk.video.get(videos=f'{video_owner_id}_{video_post_id}_{video_access_key}')
                video_url = video["items"][0]["player"]
                domain = video_url.split('.')[1]
                if domain == 'youtube':
                    token = video_url.split('/')[4].split('?')[0]
                    url = f'https://www.youtube.com/watch?v={token}'
                    await dp.bot.send_message('-1001554248300', f"{a[0]['text'].split('#')[0]}\n"
                                                                f"{url}")
            elif post[0]['type'] == 'photo':
                path = f"{group_name}/files/{post_id}"
                if not os.path.exists(path):
                    os.makedirs(path)
                try:
                    count = 0
                    for element in post:
                        res = requests.get(element['photo']['sizes'][-1]['url'])

                        with open(f"{group_name}/files/{post_id}/{count}.jpg", "wb") as img_file:
                            img_file.write(res.content)

                        count += 1
                    media = types.MediaGroup()
                    for filename in os.listdir(path):
                        media.attach_photo(types.InputFile(f'{path}/{filename}'),
                                           caption=a[0]['text'] if filename == '0.jpg' else '')
                    await dp.bot.send_media_group('-1001554248300', media=media)
                    time.sleep(10)
                except KeyError:
                    print(post)

        else:
            print("Исключение")
            print(a)
