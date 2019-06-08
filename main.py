# main.py

import winreg

# 获取桌面路径
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]
desktopPath = get_desktop()

getOpenFile = input("请输入歌词路径（包含文件名，不许带引号。可以使用$d$表示桌面）（必须以日语、中文、罗马音的形式出现）：")
openFile = getOpenFile.replace("$d$", desktopPath)

getInputType = input("请输入你的歌词的格式（r表示罗马音，j表示日语，c表示中文翻译。格式如rjc）：")

# 定义Lyrics类
class Lyrics:
    def __init__(self, inputType):
        self.inputType = inputType
    # 获取日语歌词
    def getJapanese(self, openFile):
        try:
            f = open(openFile, 'r', encoding="utf-8")
        except FileNotFoundError:
            print("没有发现文件。")
        list = f.readlines()
        f.close()
        if list[-1][-1] != "\n":
            list[-1] += "\n"
        lines = len(list)
        lyric = []
        for i in range(int(self.inputType[0]), lines, 3):
            lyric.append(list[i])
        return lyric
    # 获取中文翻译
    def getChinese(self, openFile):
        try:
            f = open(openFile, 'r', encoding="utf-8")
        except FileNotFoundError:
            print("没有发现文件。")
        list = f.readlines()
        f.close()
        if list[-1][-1] != "\n":
            list[-1] += "\n"
        lines = len(list)
        lyric = []
        for i in range(int(self.inputType[1]), lines, 3):
            lyric.append(list[i])
        return lyric
    # 获取罗马音
    def getRoman(self, openFile):
        try:
            f = open(openFile, 'r', encoding="utf-8")
        except FileNotFoundError:
            print("没有发现文件。")
        list = f.readlines()
        f.close()
        if list[-1][-1] != "\n":
            list[-1] += "\n"
        lines = len(list)
        lyric = []
        for i in range(int(self.inputType[2]), lines, 3):
            lyric.append(list[i])
        return lyric

inputTypeNum = ""
for i in getInputType:
    if i == "j":
        inputTypeNum += '0'
    elif i == "c":
        inputTypeNum += '1'
    elif i == "r":
        inputTypeNum += '2'

lyrics = Lyrics(inputTypeNum)
japaneseLy = lyrics.getJapanese(openFile)
chineseLy = lyrics.getChinese(openFile)
romanLy = lyrics.getRoman(openFile)

getOutputFile = input("请输入输出路径（包含文件名，可以使用$d$表示桌面）：")
getOutputFile = getOutputFile.replace("$d$", desktopPath)

getOutputType = input("有多种输出方式，r表示罗马音，j表示日语，c表示中文翻译。请输入输出方式（如rjc）：")

lines = len(japaneseLy)
f = open(getOutputFile, "w", encoding = "utf-8")

for i in range(0, lines):
    for direct in range(0, 3):
        if getOutputType[direct] == "r":
            f.write(romanLy[i])
        if getOutputType[direct] == "j":
            f.write(japaneseLy[i])
        if getOutputType[direct] == "c":
            f.write(chineseLy[i])

tip = input("输出完成。按回车退出。")
