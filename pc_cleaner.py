import os
import glob
import shutil

dict_group={'xlsx':[['*.xlsx','*.xls'],"\\Archivos_XLSX"],'pdf':[['*.pdf'],"\\Archivos_PDF"],'img':[['*.jpg','*.jpeg','*.png','*.gif'],"\\Archivos_IMG"],'videos':[['*.mp4','*.avi','*.mkv','*.wmv'],"\\Archivos_Videos"],'exe':[['*.exe'],"\\Archivos_exe"],'ppt':[['*.pptx'],"\\Archivos_ppt"],'zip':[['*.zip','*.rar','*.tar','*.gz','*.7z'],"\\Archivos_zip"],'txt':[['*.txt','*.csv','*.docx'],"\\Archivos_txt"]}
list_det_files=['.xlsx','.xls','.pdf','.jpg','.jpeg','.png','.gif','.mp4','.avi','.mkv','.wmv','.exe','.pptx','.zip','.rar','.tar','.gz','.7z','.txt','.csv','.docx']
clean_path=[]
single=[]
flag_path='1'
method=input('Digita 1 o 2 depende de qué utilidad desee:\n 1.Sencillo: Escoges una o varios carpetas para organizar y te agrupa los archivos sobrantes en la misma carpeta.\n 2.Por definir.\n')
while(flag_path=='1'):
    clean_path.append(input('Digita el path de donde se encuentre la carpea que quieras limpiar ej:\n ‪C:\\Users\\Pythonibiris\\OneDrive\\Documents\n').replace('\u202a', ''))
    flag_path=input('Digite 1 o 2 si desea agregar otra carpeta para limpiar? 1.si 2.no\n')
if method=='1':
    for path in clean_path:
        for key,value in dict_group.items():
            for types in value[0]:
                single+=glob.glob(os.path.join(path, types))
            dict_group[key].append(single)
            single=[]
        for create in dict_group.values():
            if not os.path.exists(path+create[1]):
                os.makedirs(path+create[1])
            if not os.path.exists(path+'\\Otros_archivos'):
                os.makedirs(path+'\\Otros_archivos')
        for move in dict_group.values():
            for files in move[2]:
                name_file=files.split("\\")[-1]
                if os.path.exists(path+move[1]+"\\"+name_file):
                    print("Hey this file: "+ files +" already exists in: "+ path+move[1])
                else:
                    shutil.move(files, path+move[1])
        last=glob.glob(os.path.join(path, '*.*'))
        noini = [archivo for archivo in last if 'desktop.ini' not in archivo.lower()]
        for files in last:
            if any(types in files for types in list_det_files):
                pass
            else:        
                name_file=files.split("\\")[-1]
                if os.path.exists(path+"Otros_archivos\\"+name_file):
                    print("Hey this file: "+ files +" already exists in: "+ path+"\\Otros_archivos")
                else:
                    shutil.move(files, path+'\\Otros_archivos')
        input("Press any key to quit the session")
elif method=='2':
    pass
else:
    print('Opción no disponible, vuelve a ejecutar el programa')
    
