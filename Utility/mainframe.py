from tkinter import *

class MainFrame():
    
    def __init__(self, root):
        # Set root
        self.root = root

        # Initailize place Option
        self.x = -1
        self.y = -1
        self.width, self.height = root.size()

        # Initailize Stage
        self.mode = 0

        # Create Main Frame
        self.frame = Frame(root, width=self.width, height=self.height, highlightbackground='black', highlightthickness= 1)
        self.frame.place(x=self.x, y=self.y)   

        
    
    class Control_Pannel():
        def __init__(self, mainframe, list):
            #Set mainframe
            self.frame = mainframe
            self.width, self.height = self.frame.size()

             # Initailize Page Num
            self.page = 0
            self.maxpage = len(list)

            # Control Buttons Frame
            self.controlframe_height = self.height//14
            self.controlframe = Frame(self.frame, width=self.width, height=self.height//7, highlightbackground='black', highlightthickness=1, background='black')
            self.controlframe.place(x=-1, y=self.controlframe_height*12)


        def Control_Buttons(self):
            # 이전 버튼
            prev = Button(self.controlframe, text='이전', command= self.Prev, background='gray')
            prev.place(x=-1, y=-1, width=100, height=50)

            # 현재 페이지 표시
            numbers = Frame(self.controlframe,background='black')
            numbers.place(x=100, y=-1, width=250, height=self.controlframe_height)
            pages = Label(numbers, text=str(self.page) + '/' + str(self.maxpage),background='gray')
            pages.place(x=-1, y=-1, width=250, height=self.controlframe_height)

            # 다음 버튼
            next = Button(self.controlframe, text='다음', command= self.Next,background='gray')
            next.place(x=350, y=-1, width=100, height=self.controlframe_height)

            #### 확정 버튼 ####
            confirm = Button(self.controlframe, text= '확정', command=self.Confirm,background='gray')
            confirm.place(x=-1, y=self.controlframe_height - 1, width=self.width, height=self.controlframe_height)
        
        def Prev(self):
            if self.page > 1:
                self.page -= 1
                self.Update()
        def Next(self):
            if self.page < self.maxpage:
                self.page += 1
                self.Update()


        # TODO Link List and Comfirm Function
        def Confirm(self):
            # Champion Ban
            if self.frame.mode == 0:
                #Append Bannded List
            # Champion Select
            elif self.frame.mode == 1:
                #Append Selected List
            # Skin Select
            elif self.frame.mode == 2:
                #Save Data and Quit


            self.frame.mode += 1
            
                

    

    def Update(self):
        self.frame.place(x=self.x, y=self.y, width=self.width, height=self.height)
        self.Control_Pannel(self.frame, )
    def Place_Option(self, x, y, width, height ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height