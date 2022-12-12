from os.path import isdir
from os import mkdir

a = 0

if isdir("datas") == False:
    mkdir("datas")
    open("datas/checkfile.checkfile","x").close
    open("datas/passwords.csv","x").close
    for i in open("intro.txt").readlines():
        print(i)
    while a <= 100:
        print("")
        i += 1
else:
    pass

from read_and_write import reader

mode = input("if you want to read password,please type read,and you want to write password,please type write:  ")
if mode == "read":
    mode = True
elif mode == "write":
    mode = False
else:
    raise SyntaxError("you type wrong word,please reopen the program.")

if mode == True:
    sinorall = input("you want to search one or show all?  ")
    if sinorall == "one":
        sinorall = True
    elif sinorall == "all":
        sinorall = False
    if sinorall == True:
        print(reader.readone(input("what website's password do you want to get?  ")))
    elif sinorall == False:
        for i in reader.readall():
            print(i)