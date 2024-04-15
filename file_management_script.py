import os
import shutil

endpoint = ""
choose = ""

def copy_files(source_folder, destination_folder):
    global endpoint
    # Kaynak dizindeki tüm dosyaları tarayın
    for file_name in os.listdir(source_folder):
        # Dosya yolu oluşturun
        file_path = os.path.join(source_folder, file_name)
        
        # Dosya MP4 uzantılı mı kontrol edin
        if os.path.isfile(file_path) and file_name.endswith(f'.{endpoint}'):
            # Hedef dosya yolunu oluşturun
            destination_path = os.path.join(destination_folder, file_name)
            
            # Dosyayı hedef klasöre kopyalayın
            shutil.copy(file_path, destination_path)

def move_files(source_folder, destination_folder):
    # Kaynak dizindeki tüm dosyaları tarayın
    for file_name in os.listdir(source_folder):
        # Dosya yolu oluşturun
        file_path = os.path.join(source_folder, file_name)
        
        # Dosya MP4 uzantılı mı kontrol edin
        if os.path.isfile(file_path) and file_name.endswith(f'.{endpoint}'):
            # Hedef dosya yolunu oluşturun
            destination_path = os.path.join(destination_folder, file_name)
            
            # Dosyayı hedef klasöre taşıyın
            shutil.move(file_path, destination_path)


# Kullanım örneği:
# Kaynak klasör
source_folder = os.getcwd()  # Mevcut çalışma dizini


while True:
    if endpoint == "":
        endpoint = input("Whats file endswith? (example: mp4) :")
    else:
        break

destination_folder = f"{endpoint}_files"  # Hedef klasör adını belirleyin

if not os.path.exists(destination_folder): # Hedef klasör yoksa, oluşturun
    os.makedirs(destination_folder)



while True:
    if choose == "":
        choose = input("Copy (1) or Cut (2) (example: 1) :")
    elif choose == "1":
        copy_files(source_folder, destination_folder)
        print(f"{endpoint} dosyaları {destination_folder} klasörüne kopyalandı.")
        break
    elif choose == "2":
        move_files(source_folder, destination_folder)
        print(f"{endpoint} dosyaları {destination_folder} klasörüne kesildi.")
        break
    else:
        choose = input("Copy (1) or Cut (2) (example: 1) :")
    








