from utils.ImageUtil import getImageHash

class Config():
    lingdangPath = "images\lingdang.png"
    lingdangArea = (40,210,145,315)
    # lingdangPos = ((lingdangArea[0]+lingdangArea[2])/2,((lingdangArea[1]+lingdangArea[3])/2))
    lingdangHash = getImageHash(path=lingdangPath)

    canjiaPath = "images\canjia.png"
    canjiaArea = (745,2390,1330,2540)
    # canjiaPos = ((canjiaArea[0]+canjiaArea[2])/2,((canjiaArea[1]+canjiaArea[3])/2))
    canjiaHash = getImageHash(path=canjiaPath)

    zhunbeiPath = "images\zhunbei.png"
    zhunbeiArea = (410,2080,1025,2285)
    # zhunbeiPos = ((zhunbeiArea[0]+zhunbeiArea[2])/2,((zhunbeiArea[1]+zhunbeiArea[3])/2))
    zhunbeiHash = getImageHash(path=zhunbeiPath)

    jixuPath = "images\jixu.png"
    jixuArea = (490,2660,950,2790)
    # jixuPos = ((jixuArea[0]+jixuArea[2])/2,((jixuArea[1]+jixuArea[3])/2))
    jixuHash = getImageHash(path=jixuPath)
    
    goArea = (490,2660,670,2790) #继续/离开 按键区
    resetArea = (20,2860,200,3030) #返回/城镇/主角色 按键区
    