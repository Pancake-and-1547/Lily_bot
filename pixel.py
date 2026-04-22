"""
Library needed
"""
import os
import random
from pathlib import Path
from pixivpy3 import *

def lily_appoint(pixiv_id, pixiv_token):
    """
    A function used to find pics with specific pixiv_id from pixiv and store it in local file
    """
    BASE_DIR = Path(__file__).resolve().parent
    SAVE_DIR = BASE_DIR / "Lily"
    SAVE_DIR.mkdir(exist_ok=True)

    file_name = "temp_lily.jpg"
    full_path = SAVE_DIR / file_name

    # 如果文件存在，则删除给新文件留空间

    if full_path.exists():
        os.remove(full_path)

    api = AppPixivAPI()
    api.auth(refresh_token = pixiv_token)

    json_result = api.illust_detail(pixiv_id)
    illust = json_result.illust

    print(illust["image_urls"]["medium"])

    api.download(illust["image_urls"]["medium"], path = SAVE_DIR, name = file_name)
    return str(full_path)

def lily_generate(pixiv_token):
    """
    find a random lily pic
    """
    BASE_DIR = Path(__file__).resolve().parent
    SAVE_DIR = BASE_DIR / "Lily"
    SAVE_DIR.mkdir(exist_ok=True)

    file_name = "temp_lily.jpg"
    full_path = SAVE_DIR / file_name

    # 如果文件存在，则删除给新文件留空间

    if full_path.exists():
        os.remove(full_path)

    api = AppPixivAPI()
    api.auth(refresh_token = pixiv_token)

    random_offset = random.randint(0,100)
    search_word = "百合 1000users入り -R-18 -漫画"

    json_result = api.search_illust(
        search_word,
        search_target = "partial_match_for_tags",
        sort = "date_desc",
        offset = random_offset
    )

    if json_result.illusts:
        # 1. 使用列表推导式，筛选出只有 1 页的作品
        single_pics = [i for i in json_result.illusts if i.page_count == 1]
        if single_pics:
            # 2. 从筛选后的单图列表中随机选一张
            illust = random.choice(single_pics)
        else:
            # 如果这一页全是组图（概率很低），就保底选第一张
            illust = json_result.illusts[0]

    if json_result.illusts:
        illust = random.choice(json_result.illusts)
    else:
        return None

    print(illust["image_urls"]["medium"])

    api.download(illust["image_urls"]["medium"], path = SAVE_DIR, name = file_name)
    return str(full_path)


if __name__ == "__main__":
    # lily_generate()
    pass
