import os, shutil

import pandas as pd

import urllib

def get_docs(document):
    doc = pd.read_csv(document)
    
    return doc
    
def download_path(document):
    links1 = document['img_0_link']
    links2 = document['img_1_link']
    
    path_list1 = []
    path_list2 = []
    
    
    for row in links1.index:
       path = "./" + str(document['numero'][row]) + "/Dados.txt"
       path_list1.append(links1[row])
       
       if os.path.exists(str(document['numero'][row])):
           shutil.rmtree(str(document['numero'][row]))
           os.mkdir(str(document['numero'][row]))
           
       else:    
           os.mkdir(str(document['numero'][row]))

       
    for row in links2.index:
        path = "./" + str(document['numero'][row]) + "/Dados.txt"
        path_list2.append(links2[row])
       
        if os.path.exists(str(document['numero'][row])):
            shutil.rmtree(str(document['numero'][row]))
            os.mkdir(str(document['numero'][row]))
           
        else:    
            os.mkdir(str(document['numero'][row]))
        
       
        with open(path, 'w') as files:
           files.write(str(document["car_ids"][row]) + '\n')
           files.write(str(document["desm_in_car_area"][row]) + '\n')
           files.write(str(document["desm_in_car_perc"][row]) + '\n')
           files.write(str(document["desm_in_sigef_c_area"][row]) + '\n')
           files.write(str(document["desm_in_sigef_c_perc"][row]) + '\n')
           files.write(str(document["desm_in_sigef_r_area"][row]) + '\n')
           files.write(str(document["desm_in_sigef_r_perc"][row]) + '\n')
           files.write(str(document["desm_in_snci_area"][row]) + '\n')
           files.write(str(document["desm_in_snci_perc"][row]) + '\n')
           files.write(str(document["desm_in_ti_uc_area"][row]) + '\n')
           files.write(str(document["desm_in_ti_uc_perc"][row]) + '\n')
           files.write(str(document["desm_in_tl_area"][row]) + '\n')
           files.write(str(document["desm_in_tl_perc"][row]) + '\n')
           files.write(str(document["desmatamento_area"][row]) + '\n')
           files.write(str(document["img_0_date"][row]) + '\n')
           files.write(str(document["img_0_id"][row]) + '\n')
           files.write(str(document["img_1_date"][row]) + '\n')
           files.write(str(document["img_1_id"][row]) + '\n')
           files.write(str(document["numero"][row]) + '\n')
           files.write(str(document["sigef_c_ids"][row]) + '\n')
           files.write(str(document["sigef_r_ids"][row]) + '\n')
           files.write(str(document["snci_ids"][row]) + '\n')
           files.write(str(document["ti_uc_ids"][row]) + '\n')
           files.write(str(document["tl_ids"][row]) + '\n')
           files.write(str(document["desm_in_embargo_area"][row]) + '\n')
           files.write(str(document["desm_in_embargo_perc"][row]) + '\n')
           files.write(str(document["embargo_ids"][row]) + '\n')
           files.close()
    
    for i in links1.index:
        urllib.request.urlretrieve(links1[i],
                                   filename = "./" + str(document['numero'][i]) + '/Antes'  + '.png')
        urllib.request.urlretrieve(links2[i],
                                   filename = "./" + str(document['numero'][i]) + '/Depois'  + '.png')
        
        

if __name__ == "__main__":
    
    sheet = get_docs("dados_12130.csv")
    
    paths = download_path(sheet)
    