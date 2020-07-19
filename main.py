import time
import shutil
import os

# Chemin d'acces au repertoire de l'appareil photo
source = "Documents/script/repdrone/"
# Chemin d'acces au repertoire de la carte
destination = "Documents/script/attente/"

def clear_rep(repertoirepath):
    for filename in os.listdir(repertoirepath):
        os.remove(repertoirepath+"/"+filename)

def transfert_file(source_dir,source_file,dest_dir):
    existing=0
    for dest_file in os.listdir(dest_dir):
        if(source_file == dest_file):
            existing=1
    if(existing==0):
        shutil.copy(source_dir+source_file, dest_dir+source_file)
        print("copie de :"+source_dir+source_file+" vers : "+dest_dir+source_file)
    else:
        print (source_file+" deja present dans le repertoire")
        existing=0

def transfert_all(source_dir,dest_dir):
    existing=0
    for source_file in os.listdir(source_dir):
        for dest_file in os.listdir(dest_dir):
            if(source_file == dest_file):
                existing=1
        if(existing==0):
            shutil.copy(source_dir+source_file, dest_dir+source_file)
            print("copie de :"+source_dir+source_file+" vers : "+dest_dir+source_file)
        else:
            print (source_file+" deja present dans le repertoire")
            existing=0

def force_transfert_file(source_dir,source_file,dest_dir):
    shutil.copy(source_dir+source_file, dest_dir+source_file)

def force_transfert_all(source_dir,dest_dir):
    for filename in os.listdir(source_dir):
        shutil.copy(source_dir+filename, dest_dir+filename)

def transfert_delay(source_dir,dest_dir,delay):
    while (1):
        transfert_all(source,destination)
        time.sleep(delay)

 
print(os.listdir(source))
#transfert_all(source,destination)
#clear_rep(destination)
transfert_delay(source,destination,5)