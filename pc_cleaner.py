import os
import glob
import shutil

dict_group={'xlsx':[['*.xlsx','*.xls'],"\\Archivos_XLSX"],'pdf':[['*.pdf'],"\\Archivos_PDF"],'img':[['*.jpg','*.jpeg','*.png','*.gif'],"\\Archivos_IMG"],'videos':[['*.mp4','*.avi','*.mkv','*.wmv'],"\\Archivos_Videos"],'exe':[['*.exe'],"\\Archivos_exe"],'ppt':[['*.pptx'],"\\Archivos_ppt"],'zip':[['*.zip','*.rar','*.tar','*.gz','*.7z'],"\\Archivos_zip"],'txt':[['*.txt','*.csv','*.docx'],"\\Archivos_txt"]}
clean_path=[]
single=[]
flag_path='1'
method=input('Digita 1 o 2 de pende de que método de limpieza prefiere:\n 1.Sencillo: Escoges una o varios carpetas para organizar y te agrupa los archivos sobrantes en la misma carpeta.\n 2.Avanzado: Escoges ciertas carpetas y digitas ciertos paths, te lo va a origanizar por tipo de archivo ej: si es pdf va a documentos y si es .jpg va a imagenes y así.\n')
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
                shutil.move(files, path+move[1])
        last=glob.glob(os.path.join(path, '*.*'))
        noini = [archivo for archivo in last if 'desktop.ini' not in archivo.lower()]
        for files in last:
            shutil.move(files, path+'\\Otros_archivos')
elif method=='2':
    pass
else:
    print('Opción no disponible, vuelve a ejecutar el programa')
    
