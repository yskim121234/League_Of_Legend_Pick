from tkinter import *

class Champion:

    def __init__(self, name, key, img):
        self.Name = name
        self.Key = key
        self.IMG = img
        self.Is_banned = False

    Name = ''
    Key = 0
    IMG = Image()
    Is_banned = False

    def Get_Champion():
        return Champion

    def Get_Name():
        return Champion.Name
    def Set_Name(name):
        Champion.Name = name
    
    def Get_Key():
        return Champion.Key
    def Set_Key(key):
        Champion.Key = key
    
    def Get_Image():
        return Champion.IMG
    def Set_Image(img):
        Champion.IMG = img
    
    def Is_Banned():
        return Champion.Is_Banned
    def Set_Banned(bool):
        Champion.Is_Banned = bool