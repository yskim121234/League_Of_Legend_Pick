import os
import glob

def Normalization_file_name(path, option = 'lower'):
    file_list = os.listdir(path)
    if option == 'upper':
         for f in file_list:
              os.rename(path + f, path +f.upper())
    elif option == 'lower':
        for f in file_list:
                os.rename(path+f, path+f.lower())

def Normalization_file_extender(path, extender, extender_Change):
    files = glob.glob(path + '*' + extender)
    for f in files:
        if not os.path.isdir(f):
            src = os.path.splitext(f)
            os.rename(f, src[0]+ extender_Change)

def Replace_Name(path, file_Name, replace_Name):
     file_list = os.listdir(path)
     for f in file_list:
          if f.find(file_Name) == 0:
               replaced = f.replace(file_Name, replace_Name)
               os.rename(path + f, path + replaced)
