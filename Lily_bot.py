"""
Library needed
"""
import base64
import nonebot
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Adapter, MessageSegment
from pixel import lily_generate, dst_generate, scenery_generate
# from nonebot import on_command

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(Adapter)

# 插件处理

nonebot.load_builtin_plugins("echo")

Help = on_command(cmd = "help", block = True)
Lily = on_command(cmd = "lily", block = True)
Dst = on_command(cmd = "dst", block = True)
Scenery = on_command(cmd = "scenery", block = True)

config = nonebot.get_driver().config
pixiv_token = getattr(config, "pixiv_refresh_token", None)

@Lily.handle()
async def handle_lily():
    """
    用来接收 /lily 并回复的函数
    """
    image_path = lily_generate(pixiv_token)
    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
            base64_str = base64.b64encode(image_bytes).decode("utf-8")
        await Lily.send(MessageSegment.image(f"base64://{base64_str}"))
    except Exception as e:
        await Lily.send(f"图片发送失败了，报错信息为{e}")
@Dst.handle()
async def handle_dst():
    """
    用来接收 /dst 并回复的函数
    """
    image_path = dst_generate(pixiv_token)
    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
            base64_str = base64.b64encode(image_bytes).decode("utf-8")
        await Dst.send(MessageSegment.image(f"base64://{base64_str}"))
    except Exception as e:
        await Dst.send(f"图片发送失败了，报错信息为{e}")
@Scenery.handle()
async def handle_scenery():
    """
    用来接收 /scenery 并回复的函数
    """
    image_path = scenery_generate(pixiv_token)
    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
            base64_str = base64.b64encode(image_bytes).decode("utf-8")
        await Scenery.send(MessageSegment.image(f"base64://{base64_str}"))
    except Exception as e:
        await Scenery.send(f"图片发送失败了，报错信息为{e}")
@Help.handle()
async def help_handle():
    """
    一个常见的 /help 功能
    """
    string: str = (
        "这里是 bot-1553,能发图\n"
        "/lily: 发送一张随机的百合图片\n"
        "/dst: 发送一张随机的 Don't Starve Together 图片\n"
        "/scenery: 发送一张随机的风景图片\n"
        "图片来源: pixiv,已经筛选过 AI 生图了"
    )
    await Help.send(string)

if __name__ == "__main__":
    nonebot.run()

