<p align="center">
  <a href="https://github.com/KimigaiiWuyi/GenshinUID/"><img src="https://s2.loli.net/2022/01/31/kwCIl3cF1Z2GxnR.png" width="256" height="256" alt="GenshinUID"></a>
</p>
<h1 align = "center">MoePoke(萌戳)</h1>
<h4 align = "center">✨基于<a href="https://github.com/nonebot/nonebot2" target="_blank">NoneBot2</a>的戳一戳插件✨</h4>

## 丨我该如何安装该插件？

```shell
# clone至插件文件夹即可
git clone https://ghproxy.com/https://github.com/KimigaiiWuyi/MoePoke.git
```
## 丨命令

`切换主题`：内置`派蒙`, `可莉`两个主题，你也可以直接放入符合结构的主题文件夹

`戳`：直接戳Bot即可收到回复（手机端双击Bot头像）

## 丨自定义主题

你可将`MoePoke/Theme`内的文件夹视为一个主题，文件夹名字即主题名字

文件夹结构：`image`，`record`，`text.yaml`

分别对应图片，语音和文字

按照相对应目录放好，`PNG`，`JPEG`等图片文件放在image目录下

`mp3`，`ogg`等音频文件放在`record`目录下

其中`text.yaml`格式如下：

```yaml
text:
 - 来和可莉一起炸鱼吧！
```

最后，重命名文件夹名称，移至`Theme`文件夹内，假设新的自定义主题名称为`萌`

无需重启Bot，发送`切换主题 萌`即可完成切换主题

## 丨其他

+ 如果对本插件有功能建议&Bug报告，欢迎提Issue & Pr，每一条都会详细看过
+ 如果本插件对你有帮助，不要忘了点个Star~
+ 本项目仅供学习使用，请勿用于商业用途
+ 欢迎贡献主题喵~
+ [爱发电](https://afdian.net/@KimigaiiWuyi)
+ [GPL-3.0 License](https://github.com/KimigaiiWuyi/GenshinUID/blob/main/LICENSE) ©[@KimigaiiWuyi](https://github.com/KimigaiiWuyi)
