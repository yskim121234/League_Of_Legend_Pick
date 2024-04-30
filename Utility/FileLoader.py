import json
from PIL import ImageTk, Image
#챔피언 정보 파일 읽어오고 문자열로 캐스팅
with open('./dragontail-14.7.1/14.7.1/data/en_US/champion.json', encoding='UTF-8') as Champion_Info:
    Champion_Info = str(json.load(Champion_Info))


class File_Loader:

    def __init__(self):
        self.Champions = []

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
    
