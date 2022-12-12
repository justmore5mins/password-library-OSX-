from touch_id.touchid import authenticate
from os.path import isdir
from os import mkdir

class logger:
    def logger(reason:str,useragent:list[str]):
        if authenticate(reason=reason) == True and len(open("system_datas/useragent.csv").readlines()) == 2:
            return True
        elif len(open("system_datas/useragent.csv").readlines()) > 2:
            if useragent in open("system_datas/useragent.csv").readlines():
                return True
            else:
                return False
        else:
            return False

def checkusetime():
    dirpath = "system_datas"
    filespath = [r"system_datas/checkfile.checkfile",r"system_datas/useragent.csv"]
    if isdir(dirpath) == False:
        mkdir(dirpath)
        for i in filespath:
            open(i,mode="x").close
        open("system_datas/useragent.csv","a").write("username,passwords")