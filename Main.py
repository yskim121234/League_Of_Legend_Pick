from Champion import Champion
import tkinter as tk
from PIL import ImageTk, Image
from functools import partial
from random import *

#챔피언 선택 프레임
def Select_Frame():

    # 최상위 프레임
    frame = tk.Frame(root, width=430, height=700, highlightbackground='black', highlightthickness= 1)
    frame.place(x=425, y=10)    

    currpage = page.get()
    ####### 챔피언 리스트 #########
    championframe = tk.Frame(frame, width=450, height=580,background='black', highlightbackground='black', highlightthickness=1)
    championframe.place(x=-1, y=-1)

    
    start = (currpage-1)*35
    champion_button =[]
    for i in range(35*5):
        if i < 167:
            if champions[i].Is_banned:
                champion_button.append(
                    tk.Button(championframe, width=80, padx=5, height=80, pady=5, image= champions[i].Image, background= 'red'))
            else:
                champion_button.append(
                    tk.Button(championframe, width=80, padx=5, height=80, pady=5, image= champions[i].Image, background= 'black', command= partial(ChampionButton, i)))
        else:
            champion_button.append(
                tk.Button(championframe, width=80, padx=5, height=80, pady=5, image= champions[167].Image, background='black'))

    if selected.get() > -1:
        champion_button[selected.get()].config(background='yellow')

    for i in range(7):
        for j in range(5):
            champion_button[start + i*5 + j].grid(row=i*5, column=j)

    # 선택된 챔피언 테두리 강조

    #######  페이지 관리 ##########
    pageframe = tk.Frame(frame, width=450, height=50, highlightbackground='black', highlightthickness=1, background='black')
    pageframe.place(x=-1, y=600)

    # 이전 버튼
    prev = tk.Button(pageframe, text='이전', command= Prev, background='gray')
    prev.place(x=-1, y=-1, width=100, height=50)

    # 현재 페이지 표시
    numbers = tk.Frame(pageframe,background='black')
    numbers.place(x=100, y=-1, width=250, height=50)
    pages = []
    for i in range(1,6):
        pages.append(tk.Label(numbers, text=str(i),background='gray'))
    
    for i in range(5):
        pages[i].place(x=i*50, y=-1,width=50, height=50)
        if currpage == 1+i:
            pages[i].config(font='Helvetica 18 bold')
        else:
            pages[i].config(font='Helvetica 8')

    # 다음 버튼
    next = tk.Button(pageframe, text='다음', command= Next,background='gray')
    next.place(x=350, y=-1, width=100, height=50)

    #### 확정 버튼 ####
    confirm = tk.Button(frame, text= '확정', command=Confirm,background='gray')
    confirm.place(x=-1, y=650, width=430, height=50)

# 이전 버튼 바인드 함수
def Prev():
    if page.get() > 1:
        page.set(page.get()-1)
    Select_Frame()

# 다음 버튼 바인드 함수
def Next():
    if page.get() <5:
        page.set(page.get()+1)
    Select_Frame()

# 챔피언 버튼 바인드 함수
def ChampionButton(index):
    selected.set(index)
    Select_Frame()

# 확인 버튼 바인드 함수
def Confirm():
    if mode.get() == 0:
        ChampionBan(selected.get())
        mode.set(1)
        Ban_Frame()
        Select_Frame()
    elif mode.get() == 1:
        Pick_Champion()
        mode.set(2)
    elif mode.get() == 2:
        Save_Data()

# 챔피언 밴
def ChampionBan(index):
    bannded.append(index)
    while len(bannded) < 10:
        rand = randint(0, 167)
        if bannded.count(rand) < 1:
            bannded.append(rand)
    
    for ban in bannded:
        champions[ban].Is_banned = True

# 밴 프레임
def Ban_Frame():
    frame1 = tk.Frame(root, highlightbackground='blue', highlightthickness= 1, background='black')
    frame2 = tk.Frame(root, highlightbackground='red', highlightthickness= 1, background='black')

    frame1.place(x= 10, y=10, width= 400, height= 90)
    frame2.place(x= 870, y=10, width= 400, height= 90)

    #밴이 진행되었을 경우 챔피언 이미지 포함, 그렇지 않을 경우 미포함
    if len(bannded) == 10:
        bannded_champion1 = []
        for i in range(5):
            bannded_champion1.append(tk.Label(frame1, image=champions[bannded[i]].Image, background='black',padx=1, pady=5, width=70, height=70))
        
        bannded_champion2 = []
        for i in range(5, 10):
            bannded_champion2.append(tk.Label(frame2, image=champions[bannded[i]].Image, background='black',padx=10, pady=5, width=70, height=70))
        
        for i in range(5):
            bannded_champion1[i].place(x=i*70+i*10, y=10)
            bannded_champion2[i].place(x=i*70+i*10, y=10)
    else:
        bannded_champion1 = []
        for i in range(5):
            bannded_champion1.append(tk.Label(frame1, image=champions[167].Image, background='black',padx=1, pady=5, width=70, height=70, highlightbackground= 'blue', highlightthickness= 1))
        
        bannded_champion2 = []
        for i in range(5, 10):
            bannded_champion2.append(tk.Label(frame2, image=champions[167].Image, background='black',padx=10, pady=5, width=70, height=70, highlightbackground= 'red', highlightthickness= 1))
        
        for i in range(5):
            bannded_champion1[i].place(x=i*70+i*10, y=10)
            bannded_champion2[i].place(x=i*70+i*10, y=10)

# 챔피언 선택
def Pick_Champion():
    if bannded.count(selected.get()) == 0:
        picked_Champions1.append(selected.get())
        
        while len(picked_Champions1) < 5:
            rand = randint(0, 167)
            if picked_Champions1.count(rand) == 0 and bannded.count(rand) == 0:
                picked_Champions1.append(rand)
        
        while len(picked_Champions2) <5:
            rand = randint(0, 167)
            if picked_Champions1.count(rand) == 0 and picked_Champions2.count(rand) == 0 and bannded.count(rand) == 0:
                picked_Champions2.append(rand)

        Player_Frame()

        

# 플레이어들 정보
def Player_Frame():
    

    players_Frame1 = tk.Frame(root, highlightbackground= 'blue', highlightthickness= 1, background= 'black')
    players_Frame2 = tk.Frame(root, highlightbackground='red', highlightthickness= 1, background= 'black')

    players_Frame1.place(x= 10, y= 110, width= 400, height= 500)
    players_Frame2.place(x= 870, y= 110, width= 400, height= 500)

    players1 = [tk.Frame(players_Frame1, highlightbackground= 'blue', highlightthickness= 1) for i in range(5)]
    players2 = [tk.Frame(players_Frame2, highlightbackground= 'red', highlightthickness= 1) for i in range(5)]

    for i in range(5):
        players1[i].place(x= -1, y= -1 + i*100, width= 400, height= 100)
        players2[i].place(x= -1, y= -1 + i*100, width= 400, height= 100)

    picked_Champions = []
    #IMG = ImageTk.PhotoImage(Image.open('./dragontail-14.7.1/14.7.1/img/champion/Default.png').resize((90, 90)))
    IMG = champions[167].Image

    player_names= []
    
    for i in range(10):
        if i == 0:
            player_names.append(tk.Label(players1[i], text ='플레이어 (1번 소환사)'))
        elif i < 5:
            player_names.append(tk.Label(players1[i], text = str(i+1)+'번 소환사'))
        else:
            player_names.append(tk.Label(players2[i-5], text = str(i+1)+'번 소환사'))
    
    for pn in player_names:
        pn.place(x=100 -1 , y= 5 -1, width = 200, height = 90)

    # 블루팀의 선택 챔피언을 등록
    for i in range(len(picked_Champions1)):
        picked_Champions.append(tk.Label(players1[i], image= champions[picked_Champions1[i]].Image))
    for i in range(5-len(picked_Champions1)):
        picked_Champions.append(tk.Label(players1[i+ len(picked_Champions1)], image= IMG))

    # 레드팀의 선택 챔피언을 등록
    for i in range(len(picked_Champions2)):
        picked_Champions.append(tk.Label(players2[i], image= champions[picked_Champions2[i]].Image))
    for i in range(5-len(picked_Champions2)):
        picked_Champions.append(tk.Label(players2[i+ len(picked_Champions2)], image= IMG))
    
    # 선택 챔피언의 이미지를 각 팀의 프레임에 띄움
    for i in range(5):
        picked_Champions[i].place(x= 5 - 1, y= 5 - 1, width = 90, height = 90)
        picked_Champions[i+5].place(x= 296 , y= 5 - 1, width = 90, height = 90)

def Save_Data():
    file = open('./Result.txt', 'w')
    file.write('{Blue Team Ban}\n')
    for i in range(5):
        if i < 4:
            file.write(champions[bannded[i]].Name + ', ')
        else:
            file.write(champions[bannded[i]].Name + '\n')

    file.write('{Blue Team Pick}\n')
    for i in range(5):
        if i < 4:
            file.write(champions[picked_Champions1[i]].Name + ', ')
        else:
            file.write(champions[picked_Champions1[i]].Name + '\n')

    file.write('{Red Team Ban}\n')
    for i in range(5):
        if i < 4:
            file.write(champions[bannded[i+5]].Name + ', ')
        else:
            file.write(champions[bannded[i+5]].Name + '\n')

    file.write('{Red Team Pick}\n')
    for i in range(5):
        if i < 4:
            file.write(champions[picked_Champions2[i]].Name + ', ')
        else:
            file.write(champions[picked_Champions2[i]].Name + '\n')
    file.close()

    


window = tk.Tk()
window.title('League of Legend')
window.geometry('1280x720')

root = tk.Frame(window, background='black')
root.place(x=-1,y=-1, width=1280, height=720)

page = tk.IntVar()
page.set(1)

selected = tk.IntVar()
selected.set(0)

mode = tk.IntVar()
mode.set(0)

champions = [Champion(i) for i in range(168)]
bannded = []

picked_Champions1 = []
picked_Champions2 = []
#### 챔피언 밴 단계 ####
Select_Frame()

Ban_Frame()

#### 챔피언 선택 단계 ####
Player_Frame()

root.mainloop()