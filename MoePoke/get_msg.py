import random
from pathlib import Path
from typing import Tuple, Union

import yaml

from .moe_conifg import MoePokeConfig

THEME_PATH = Path(__file__).parent / 'Theme'
THEME_LIST = [i for i in THEME_PATH.iterdir()]


class PokeTheme:
    def __init__(self) -> None:
        default_theme = THEME_PATH / MoePokeConfig.get_config('Theme')
        if default_theme.exists():
            self.THEME = default_theme
        else:
            self.THEME = THEME_LIST[0]

        self.THEME_ITEM = {}
        self.init_theme()

    async def change_theme(self, name: str) -> str:
        path = THEME_PATH / name
        if path.exists():
            self.THEME = path
            MoePokeConfig.set_config('Theme', name)
            self.init_theme()
            return f'修改主题 {name} 成功！'
        else:
            return f'主题 {name} 不存在！'

    def init_theme(self):
        img = self.THEME / 'image'
        text = self.THEME / 'text.yaml'
        with open(text, "r", encoding="utf-8") as ymlfile:
            text = yaml.load(ymlfile, Loader=yaml.SafeLoader)
            text = text['text']
        record = self.THEME / 'record'
        for image in img.iterdir():
            self.THEME_ITEM[image] = 'image'
        for re in record.iterdir():
            self.THEME_ITEM[re] = 'record'
        for t in text:
            self.THEME_ITEM[t] = 'text'

    async def get_item(self) -> Tuple[Union[str, Path], str]:
        item = random.choice(list(self.THEME_ITEM.keys()))
        item_type = self.THEME_ITEM[item]
        return item, item_type


Poke = PokeTheme()
