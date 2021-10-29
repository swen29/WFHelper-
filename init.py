from Config import Config
from PIL import Image
from utils.ADBUtil import *
from utils.ImageUtil import getImageHash, readImageFromBytes

while 1:
    flag = int(input())
    getScreen("images\\test.png")
    screen=Image.open("images\\test.png")
    if flag == 1:
        screen.crop((40,210,145,315)).save("test\\lingdang.png")
    if flag == 2:
        screen.crop((745,2390,1330,2540)).save("test\\canjia.png")
    if flag == 3:
        screen.crop((415,2085,1020,2280)).save("test\\zhunbei.png")
    if flag == 4:
        screen.crop((490,2660,950,2790)).save("test\\jixu.png")

        
    
    