from Config import Config
from utils.ADBUtil import *
import time
from utils.ImageUtil import getImageHash, readImageFromBytes

while 1:
    touchScreen(Config.resetArea)#预防各种意外 一定程度上防烧屏
    screen = readImageFromBytes(getScreen())
    tmp = screen.crop(Config.lingdangArea)
    hash = getImageHash(image=tmp)
    if hash != Config.lingdangHash: #反选模式，抢车更快
        print("滴滴?")
        touchScreen(Config.lingdangArea)
        time.sleep(1)
        touchScreen(Config.canjiaArea)
        print("参加!")
        time.sleep(3)
        screen = readImageFromBytes(getScreen())
        tmp = screen.crop(Config.zhunbeiArea)
        hash = getImageHash(image=tmp)
        if hash == Config.zhunbeiHash:
            touchScreen(Config.zhunbeiArea)
            print("准备!")
            time.sleep(30)#战斗中
            while 1:
                screen = readImageFromBytes(getScreen())
                tmp = screen.crop(Config.jixuArea)
                hash = getImageHash(image=tmp)
                if hash == Config.jixuHash:
                    for i in range(10):
                        touchScreen(Config.goArea)
                        time.sleep(1)
                    break
        else:
            print("迟了~")
            

