from tkinter import *
from Utility.FileLoader import File_Loader

class Champion:

    def __init__(self, index):
        self.Index = index
        self.fileLoader = File_Loader()
        self.Name = self.fileLoader.Get_Champion_Name(index)
        self.Image =  self.fileLoader.Get_Champion_Image(index)
        self.Is_banned = False
        self.Skins = self.fileLoader.Get_Champion_Skin_Dict(index)
        self.Skins_Name = self.fileLoader.Get_Skin_Name(index)
        self.Current_Skin = 0
        self.Current_Skin_Image = self.fileLoader.Get_Champion_Skin_Image(index, self.Current_Skin)
        self.loading_Image = self.fileLoader.Get_Champion_Loading_Image(index, self.Current_Skin)
    
    def Set_Current_Skin(self, i):
        self.Current_Skin = i
        self.Current_Skin_Image = self.fileLoader.Get_Champion_Skin_Image(self.Index, self.Current_Skin)
        self.loading_Image = self.fileLoader.Get_Champion_Loading_Image(self.Index, self.Current_Skin)

if __name__ == '__main__':
    window = Tk()
    window.title('Champion Class Test')
    window.geometry('500x700')

    i = int(input("Enter Champion\'s index\n=>"))
    champ = Champion(i)

    champ_Image = Label(window, image= champ.Image)
    champ_Image.place(x=0, y=0, width= 200, height=200)

    print(champ.Skins)

    while 1:
        s = int(input("Select Skin\n=>"))
        champ.Set_Current_Skin(s)
        champ_skin = Label(window, image= champ.Current_Skin_Image)
        champ_skin.place(x=0, y=200)

    window.mainloop()
