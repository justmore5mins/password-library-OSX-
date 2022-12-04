import tkinter as tk
from os.path import isfile
import UserOperate as uo

wellcome_win = tk.Tk()

wellcome_win.title("wellcome page")
wellcome_win.geometry("500x500")

wellcome_win.mainloop()

if isfile("datas/checkfile.checkfile") == False:

    tk.Label(text="First time to use app?").pack()
    tk.Label(text="let me to tech you!").pack()
    tk.Label(text="it don't upload datas to the sever.").pack()
    tk.Label(text="not happy?").pack()
    tk.Label(text="go to https://github.com/justmore5mins/password-library-OSX-/issues/new to make a issue").pack()
    tk.Button(text="continue",command=uo.add_and_delete_user.add_user())