import asyncio
import uuid
from pathlib import Path
from f2.apps.douyin.utils import create_or_rename_user_folder
from f2.apps.douyin.db import AsyncUserDB
from f2.apps.douyin.handler import DouyinHandler
from f2.apps.douyin.utils import AwemeIdFetcher
from config import cookie,pathDir
from downImage import download_image

kwargs = {
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "Referer": "https://www.douyin.com/",
    },
    "proxies": {"http": None, "https": None},
    "cookie": cookie
}


class DouyinHandlerRe(DouyinHandler):

    async def get_or_add_user_data(self, kwargs: dict, sec_user_id: str, db: AsyncUserDB, ) -> Path:
        local_user_data = await db.get_user_info(sec_user_id)

        current_user_data = await self.handler_user_profile(sec_user_id)

        current_nickname = kwargs.get("idNum")

        user_path = create_or_rename_user_folder(
            kwargs, local_user_data, current_nickname
        )

        if not local_user_data:
            await db.add_user_info(**current_user_data._to_dict())
        self.userPathDir = user_path
        return user_path


async def main(url):
    global kwargs
    id = await AwemeIdFetcher.get_aweme_id(url)
    item = await DouyinHandler(kwargs).fetch_one_video(aweme_id=id)
    itemDict = item._to_dict()
    imagesCount = len(itemDict['images'])

    if imagesCount > 0:
        print('image')
        imagesList = itemDict['images']
        dir = pathDir + '/douyin' + f'/image-{str(uuid.uuid1())}' + f'/{id}'
        for link in imagesList:
            download_image(link, dir, uuid.uuid1().__str__())
        return str(dir)

    else:
        print('video')
        kwargs["url"] = 'https://www.douyin.com/video/' + id
        kwargs["interval"] = 'all'
        kwargs["path"] = pathDir
        kwargs["mode"] = 'video-' + uuid.uuid1().__str__()
        kwargs["idNum"] = id
        dy = DouyinHandlerRe(kwargs)
        await dy.handle_one_video()

        for p in dy.userPathDir.iterdir():
            p.rename(p.parent/(uuid.uuid1().__str__()+p.suffix))
            return str(p.parent)


if __name__ == "__main__":
    r = ''
    p = asyncio.run(main(r))