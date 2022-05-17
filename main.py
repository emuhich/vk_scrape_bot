import os
import vk_api

from dotenv import load_dotenv

load_dotenv()

VK_BOT_TOKEN = str(os.getenv("VK_BOT_TOKEN"))


def main():
    vk_session = vk_api.VkApi(token=VK_BOT_TOKEN)
    vk = vk_session.get_api()
    a = vk.wall.get(owner_id=-194944166, count=5, offset=22228)
    print(a)


if __name__ == '__main__':
    main()
