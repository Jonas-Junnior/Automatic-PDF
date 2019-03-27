import os , sys, shutil

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from google_drive_downloader import GoogleDriveDownloader as gdd

def get_docs(document):
    doc = pd.read_excel(document)
    
    return doc
    
def download_path(document):
    links = document['Path']
    
    path_list = []
    id_list = []
    
    for row in links.index:
       path = "./" + str(document['ID'][row]) + "/Dados.txt"
       path_list.append(links[row])
       
       if os.path.exists(str(document['ID'][row])):
           shutil.rmtree(str(document['ID'][row]))
           os.mkdir(str(document['ID'][row]))
           
       else:    
           os.mkdir(str(document['ID'][row]))

       id_list.append(path_list[row].split('/', path_list[row].count('/'))[5])
       
       with open(path, 'w') as files:
           files.write("Name: " + str(document["Name"][row]) + '\n')
           files.write("ID: " + str(document["ID"][row]) + '\n')
           files.write("Date: " + str(document["Date"][row]) + '\n')
           files.write("Location: " + str(document["Location"][row]) + '\n')
           files.write("Size: " + str(document["Size"][row]) + '\n')
           files.write("Owner: " + str(document["Owner"][row]) + '\n')
           files.close()
    
    for i in range(len(id_list)):
        gdd.download_file_from_google_drive(file_id = id_list[i],
                                            dest_path = "./" + str(document['ID'][i]) + '/arq' + str(i))
        
        

if __name__ == "__main__":
    
    sheet = get_docs("test.xlsx")
    
    paths = download_path(sheet)
    