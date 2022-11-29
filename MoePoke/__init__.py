from nonebot import on_command, on_notice
from nonebot.adapters.onebot.v11 import Message, MessageSegment, PokeNotifyEvent
from nonebot.log import logger
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.rule import to_me

from .get_msg import Poke

poke = on_notice(rule=to_me())
change = on_command('更换主题', aliases={'切换主题', '修改主题'})


@poke.handle()
async def send_poke_pic(matcher: Matcher, event: PokeNotifyEvent):
    logger.info('收到戳一戳！')
    msg, msg_type = await Poke.get_item()
    if isinstance(msg, str):
        await matcher.finish(MessageSegment.text(msg))
    else:
        with open(msg, 'rb') as f:
            if msg_type == 'image':
                await matcher.finish(MessageSegment.image(f.read()))
            else:
                await matcher.finish(MessageSegment.record(f.read()))


@change.handle()
async def send_change_msg(matcher: Matcher, args: Message = CommandArg()):
    im = await Poke.change_theme(str(args[0]))
    await matcher.finish(MessageSegment.text(im))
