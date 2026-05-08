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

def pic_generate(random_number, search_word, pixiv_token):
    """
    a function to generate pics from pixiv and save it in the full_path
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

    random_offset = random.randint(0, random_number)
    # search_word = "百合 1000users入り -R-18 -漫画"

    json_result = api.search_illust(
        search_word,
        search_target = "partial_match_for_tags",
        sort = "date_desc",
        offset = random_offset
    )

    if json_result.illusts:
        # 1. 使用列表推导式，筛选出只有 1 页的作品
        single_pics = [i for i in json_result.illusts if i.page_count == 1 and i.illust_ai_type == 1]
        if single_pics:
            # 2. 从筛选后的单图列表中随机选一张
            illust = random.choice(single_pics)
            api.download(illust["meta_single_page"]["original_image_url"], path = SAVE_DIR, name = file_name)
        else:
            # 如果这一页全是组图（概率很低），就保底选第一张
            illust = json_result.illusts[0]
            api.download(illust["meta_pages"][0]["image_urls"]["original"], path = SAVE_DIR, name = file_name)
        if illust:
            pass
            # print(illust)
        else:
            print("Something wrong here")

    else:
        return None
    return str(full_path)

def lily_generate(pixiv_token):
    """
    a function to generate lily-pics by using pic-generate func
    """
    return pic_generate(1000, "百合 1000users入り -R-18 -漫画", pixiv_token)
def dst_generate(pixiv_token):
    """
    a function to generate dst-pics by using pic-generate func
    """
    return pic_generate(200, "Don'tStarve -R-18 -漫画", pixiv_token)
def scenery_generate(pixiv_token):
    """
    a function to generate scenery-pics by using pic-generate func
    """
    return pic_generate(1000, "風景 1000users入り -R-18 -漫画", pixiv_token)
def tickle_generate(pixiv_token):
    """
    a function to generate tk-pics by using pic-generate func
    Only for personal use, not going to put it in the lily-bot
    """
    return pic_generate(200, "tickle -漫画", pixiv_token)

if __name__ == "__main__":
    tickle_generate("HX-4Pdb-D5_ORZff5yqxLD9oawEu9N2E_8y_iegEBdE")
