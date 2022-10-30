# 语音数据集制作标注工具

## 简介

用于从音频文件和srt字幕文件开始制作数据集，用户可以相对方便的在图形界面中编辑数据信息并导出。

初衷是用于给阿里云的语音识别系统输出可用的数据集以提高识别效果，也许还有别的用处。

界面：PySide6

数据存储：sqlite

## 开始

### 1.安装依赖

#### 直接下载最新的release文件

在[这里](https://github.com/kslz/SoundLabel/releases)下载最新release的zip压缩包，然后解压双击exe文件即可使用，不过你还是需要安装[ffmpeg](https://ffmpeg.org/download.html#get-packages)

#### 或者从源代码运行

你需要 python3 环境和配置好的 [ffmpeg](https://ffmpeg.org/download.html#get-packages)

运行`pip install -r requirements.txt` 安装所需依赖，如果你所在的地区网络不好可以尝试指定源，比如： `pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/`

你也许会安装 pyaudio 失败，请在 [这里](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) 下载对应版本的 whl 文件，我在根目录下也放了一个 whl 文件，如果你的python版本是3.9的话可以直接使用。得到whl文件后运行`pip install xxx.whl`安装。

### 2.准备数据

① 请准备一个音频文件（支持wav，mp3，acc格式）和一个与之同名的srt文件，两个文件名之间只能有后缀名不同。

② 在项目根目录下新建一个文件夹`filepath` 将srt文件和音频文件放入其中

### 3.运行项目

运行 `python main.py` 

## 功能介绍

### 主界面：

![主界面](https://github.com/kslz/SoundLabel/blob/master/img/main1.png?raw=true)

- 点击上方的【导入字幕文件和音频文件】按钮可以进入导入界面
- 表格中展示了已有的数据集，点击【进入】按钮可以跳转到对应数据集的编辑页，点击【导出数据集】按钮可以将已标注且标注为可用的数据导出，导出路径为： `filepath/output/数据集名_日期时间/`
![主界面](https://github.com/kslz/SoundLabel/blob/master/img/main2.png?raw=true)
- 点击删除按钮可以删除对应数据集（没有真的删除，可以从sqlite中找回）
- 被导入的数据会记录音频文件的位置，请不要移动或删除。当对应的音频文件找不到时数据集会不可用



### 导入界面

![导入界面](https://github.com/kslz/SoundLabel/blob/master/img/input1.png?raw=true)

- 导入界面中展示了目前可导入和已有的数据集，程序会遍历`filepath`目录下的srt文件，然后寻找对应的音频文件，如果可以找到则会在表格中将其展示。点击导入按钮可以导入新的数据集。
- 数据集成功导入后srt文件就不再使用了，可以删除或移动，只保留音频文件即可。

### 标注界面

![标注界面](https://github.com/kslz/SoundLabel/blob/master/img/workspace1.png?raw=true)

标注界面比较复杂，注意：出于节约时间考虑在取数据时过滤掉了4个字和以下长度的音频

- 窗口右下角的数据列表展示了本数据集中的语句（从srt文件中提取得到），点击【跳转】可以使页面展示对应条目的音频标注信息。
- 界面上方的起止时间表示了本条音频在总音频文件中的起止时间，点击【播放音频】按钮可以试听，如果觉得切割位置不对可以修改这两个值后再点击【播放音频】试听效果。注意：如果此时不点击【确定标注】按钮，则修改的起止时间不会保存。
- 快捷调节时间按钮：点击可以快速加减起止时间
- 【刷新数据列表】按钮的功能是刷新右下角的数据列表，当你修改音频的起止时间影响到音频顺序时你可以点击这个按钮更新列表信息。我不是很推荐做这么大的改动，可能会有bug（待测试）。而且这个按钮比较吃资源，没事不要点，作者之后会想办法优化。
- 【上一条】【下一条】按钮：跳转到上一条或下一条音频信息。
- 【确定标注】按钮：将页面中的数据保存到数据库中
- 两个勾选框：功能如描述
- 标注信息：本条音频对应的文本信息。
- 是否可用：如果你觉得这条音频效果太烂了，加进去可能会影响训练效果，请选择不可用。
- 选择音频播放设备：如果需要可以在此选择，默认选择为系统默认音频设备。注意：如果打开界面后修改了系统默认音频设备，则此处会顺序错乱，请重新打开此界面。
- 导出当前音频：将目前页面上的起止时间划出的音频保存到 `filepath/output` 路径下 根据时间命名
- 【返回首页]按钮：返回首页
- 已知问题：当跳转按钮置灰时鼠标放上去滑动滚轮会无法滚动表格，作者太菜了不会改，谁知道怎么办务必教一下 感谢



## 其他

sqlite位置：db/data.db

删除数据集后找回：如图所示，将表重命名回原来的名字即可

![删除找回界面](https://github.com/kslz/SoundLabel/blob/master/img/delete_dataset.png?raw=true)











