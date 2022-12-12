import csv

file = open("passwords","a+")
class reader:
    def readone(target:str):
        data = csv.DictReader(file)
        for i in data:
            usrandpas = {i["username"]}
            