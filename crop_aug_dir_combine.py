import shutil
import os

source = '/home/hamed/project_antwerp/dataset/CUB_200_2011/train_cropped/'
dist = '/home/hamed/project_antwerp/dataset/CUB_200_2011/train_cropped_augmented/'

source_folders_dir = [os.path.join(source, folder) for folder in next(os.walk(source))[1]]
print(source_folders_dir)
for folder_dir in source_folders_dir:
    files = os.listdir(folder_dir)
    folder_name = folder_dir.split('/')[-1]
    for file in files:
        shutil.move(folder_dir+'/'+file,dist+folder_name)