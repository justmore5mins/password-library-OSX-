import csv

file = open("datas/passwords","a+")
class reader:
    def readone(website:str):
        """
        it can read one website's password and print,\n
        if the website is not exist,it will raise UserWaring error
        """
        data = csv.reader(file)
        webandpas = {}
        for datalist in list(data):
            webandpas.setdefault(datalist[0],datalist[-1])
        if webandpas.get(website) != None:
            thing = str(webandpas.get(website))
            return thing
        else:
            return UserWarning("please reopen the program to get type the website name")
    def readall():
        """
        it can read and print all webisite's name and password
        """
        data = csv.reader(file)
        return list(data)