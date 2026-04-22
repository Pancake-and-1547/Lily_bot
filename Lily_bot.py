"""
Library needed
"""
import base64
import nonebot
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Adapter, MessageSegment
from pixel import lily_generate
# from nonebot import on_command

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(Adapter)

# 插件处理

nonebot.load_builtin_plugins("echo")

Lily = on_command(cmd = "lily", block = True)

config = nonebot.get_driver().config
pixiv_token = getattr(config, "pixiv_refresh_token", None)

@Lily.handle()
async def handle_function():
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


if __name__ == "__main__":
    nonebot.run()
