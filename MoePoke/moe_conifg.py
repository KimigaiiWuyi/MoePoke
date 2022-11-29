import json
from pathlib import Path

MAIN_PATH = Path() / 'data' / 'MoePoke'
MOE_CONFIG_PATH = MAIN_PATH / 'config.json'


CONIFG_DEFAULT = {'Theme': '派蒙'}


class MoeConfig:
    def __init__(self) -> None:
        if not MOE_CONFIG_PATH.exists():
            _new = MAIN_PATH.mkdir(exist_ok=True)
            with open(MOE_CONFIG_PATH, 'w', encoding='UTF-8') as file:
                json.dump(CONIFG_DEFAULT, file, ensure_ascii=False)

        self.update_config()

    def write_config(self):
        with open(MOE_CONFIG_PATH, 'w', encoding='UTF-8') as file:
            json.dump(self.config, file, ensure_ascii=False)

    def update_config(self):
        # 打开config.json
        with open(MOE_CONFIG_PATH, 'r', encoding='UTF-8') as f:
            self.config = json.load(f)
        # 对没有的值，添加默认值
        for key in CONIFG_DEFAULT:
            if key not in self.config:
                self.config[key] = CONIFG_DEFAULT[key]

        # 重新写回
        self.write_config()

    def get_config(self, key: str) -> str:
        if key in self.config:
            return self.config[key]
        elif key in CONIFG_DEFAULT:
            self.update_config()
            return self.config[key]
        else:
            return ''

    def set_config(self, key: str, value: str) -> bool:
        if key in CONIFG_DEFAULT:
            # 设置值
            self.config[key] = value
            # 重新写回
            self.write_config()
            return True
        else:
            return False


MoePokeConfig = MoeConfig()
