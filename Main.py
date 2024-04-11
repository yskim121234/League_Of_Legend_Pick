from tkinter import *
from header.FileLoader import *
from header.WindowManager import *

#창 생성
Window = Tk()
Window.title('League of Legend')
#Window.attributes('-fullscreen', True) # 전체화면 설정
Window.geometry('1280x720')

Banned_Champion_Blue = Frame(Window, relief='solid', bd=2, width=300, height=100)
Banned_Champion_Blue.place(x=10, y=10)

Banned_Champion_Red = Frame(Window, relief='solid', bd=2, width=300, height=100)
Banned_Champion_Red.place(x=970, y=10)

Window.mainloop()