from public import useroperate
from os.path import isdir
from os import mkdir

a = 0

if isdir("datas/checkfile.checkfile") == False:
    mkdir("datas")
    open("checkfile.checkfile","x").close
    open("passwords.csv","x").close
    for i in open("public.intro.txt").readlines():
        print(i)
    while a <= 100:
        print("")
        i += 1
else:
    pass

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
