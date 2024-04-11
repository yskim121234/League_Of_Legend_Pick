import json

#챔피언 정보 파일 읽어오고 문자열로 캐스팅
with open('./dragontail-14.7.1/14.7.1/data/en_US/champion.json', encoding='UTF-8') as Champion_Info:
    Champion_Info = str(json.load(Champion_Info))

def get_Champion_Info():
    return Champion_Info

def Get_Champion_Image_Path(key):
    #key값을 통해 챔피언의 이름 찾기
    keyword = '\'key\': \''+str(key)+'\', \'name\': \''
    start_index = Champion_Info.find(keyword) + len(keyword)
    end_index = Champion_Info.find('\'',start_index)
    champion_name = Champion_Info[start_index:end_index]

    #이미지 파일의 주소 리턴
    path = './dragontail-14.7.1/14.7.1/img/champion/'+champion_name+'.png'
    return path



    