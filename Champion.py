from tkinter import *
from Utility.FileLoader import File_Loader

class Champion:

    def __init__(self, index):
        self.Index = index
        fileLoader = File_Loader()
        self.Name = fileLoader.Get_Champion_Name(index)
        self.Image =  fileLoader.Get_Champion_Image(index)
        self.Is_banned = False