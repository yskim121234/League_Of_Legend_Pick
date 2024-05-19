import json
import os
from PIL import ImageTk, Image
import tkinter
import Normalizer

#챔피언 정보 파일 읽어오고 문자열로 캐스팅
with open('./dragontail-14.7.1/14.7.1/data/en_US/champion.json', encoding='UTF-8') as Champion_Info:
    Champion_Info = str(json.load(Champion_Info))


class File_Loader:

    def __init__(self):
        path = []
        path.append('./dragontail-14.7.1/img/champion/loading/')
        path.append('./dragontail-14.7.1/14.7.1/img/champion/')
        names = {}
        names['Renata'] = 'RenataGlasc'
        names['MonkeyKing'] = 'Wukong'
        for p in path:
            for n in names.keys():
                Normalizer.Replace_Name(p, n, names[n])
            Normalizer.Normalization_file_name(p)
            Normalizer.Normalization_file_extender(p, '.jpg', '.png')
        del path
        del names
        self.Champions = []
        self.Set_Champions()

    def Set_Champions(self):

        start = 0
        end = 0
        Champion_Info.replace(',','')
        while 1:
            start = Champion_Info.find('\'id\':', end)

            if start == -1:
                break

            end = Champion_Info.find('\'key\':',start)
            id = Champion_Info[start:end]
            start = Champion_Info.find('\'name\':',end)
            key = Champion_Info[end:start]
            end = Champion_Info.find('\'title\':',start) -1
            name = Champion_Info[start:end]

            name = name.replace('\'name\': ', '')

            name = name.replace('\'', '')

            name = name.replace('\"', '')

            name = name.replace(',', '')
            
            name = name.replace(' ', '')

            name = name.replace('.', '')

            self.Champions.append(name)
        self.Champions.append('Default')


    def Get_Champions_Name(self):
        if len(self.Champions) == 0:
            self.Set_Champions()


        return self.Champions
    
    def Get_Champion_Name(self, index):
        if len(self.Champions) == 0:
            self.Set_Champions()

        return self.Champions[index]
        

    def Get_Champion_Image_Path(self, index):
        #key값을 통해 챔피언의 이름 찾기
        champion_name = self.Champions[index]
        #이미지 파일의 주소 리턴
        path = './dragontail-14.7.1/14.7.1/img/champion/'+champion_name+'.png'
        return path
    
    def Get_Champion_Image(self, index, size=80):
        return ImageTk.PhotoImage(Image.open(self.Get_Champion_Image_Path(index)).resize((size, size)))
    
    def Get_Champion_Skin_Dict(self, index):
        if index >= len(self.Champions) or index <0:
            print("[Get_Champion_Skin_Dict]:Index Value Error")
            return False
        path = './dragontail-14.7.1/img/champion/centered/'
        file_list = os.listdir(path)  
        skin_dict = {}
        skin_list = []
        
        for f in file_list:
            name = self.Champions[index].lower()
            if f.find(name+'_') == 0:
                ff = f.replace(name+'_', '')
                ff = int(ff.replace('.png', ''))
                skin_list.append(ff)
        
        skin_list.sort()
        if len(skin_list) <= 0:
            skin_list.append("NO SKIN")
        skin_dict[self.Champions[index]] = skin_list
        return skin_dict
                
    def Get_Champion_Skin_Image(self, champ_Index, skin_Index):
        if champ_Index == 167:
            ##print('Default isn\'t have a skin')
            return
        name = self.Champions[champ_Index]
        path = './dragontail-14.7.1/img/champion/centered/' + name.lower() + '_' +str(self.Get_Champion_Skin_Dict(champ_Index)[name][skin_Index]) + '.png'
        img = ImageTk.PhotoImage(Image.open(path).resize((200,100)))
        return img
    
    def Get_Champion_Loading_Image(self, champ_Index, skin_Index):
        if champ_Index == 167:
            ##print('Default isn\'t have a skin')
            return
        name = self.Champions[champ_Index]
        path = './dragontail-14.7.1/img/champion/loading/' + name.lower() + '_' +str(self.Get_Champion_Skin_Dict(champ_Index)[name][skin_Index]) + '.png'
        img = ImageTk.PhotoImage(Image.open(path).resize((430, 600)))
        return img
    
    def Get_Skin_Name(self, champ_Index):
        if champ_Index == 167:
            return
        file = open("./dragontail-14.7.1/14.7.1/data/ko_KR/champion/" + self.Champions[champ_Index].lower() + ".json", encoding='UTF-8')
        file = str(json.load(file))
        i = file.find('skins')
        j = file.find('lore',i)
        file = file[i:j]
        files = file.split(',')
        result = []
        for f in range(len(files)):
            if files[f].find('name') != -1:
                files[f] = files[f].replace(' ', '')
                files[f] = files[f].replace('\'', '')
                files[f] = files[f].replace('name', '')
                files[f] = files[f].replace(':', '')
                result.append(files[f])
        
        return result






if __name__ == '__main__':
    loader = File_Loader()
    window = tkinter.Tk()
    loader.Nomalization_file_extender('./dragontail-14.7.1/img/champion/splash/', '.jpg')