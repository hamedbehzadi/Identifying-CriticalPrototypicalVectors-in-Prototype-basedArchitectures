import Augmentor
import os


datasets_root_dir = '/home/hamed/project_antwerp/dataset/CUB_200_2011/'
dir = datasets_root_dir + 'train_cropped/'
target_dir = datasets_root_dir + 'train_cropped_augmented/'

#folders = [os.path.join(dir, folder) for folder in next(os.walk(dir))[1]]
#target_folders = [os.path.join(target_dir, folder) for folder in next(os.walk(dir))[1]]
folders = []
target_folders = []

for i in range(200):
    if i < 10:
        folders.append(dir+'00'+str(i)+'/')
        target_folders.append(target_dir+'00'+str(i)+'/')
    elif i < 100:
        folders.append(dir + '0' + str(i) + '/')
        target_folders.append(target_dir + '0' + str(i) + '/')
    else:
        folders.append(dir + str(i) + '/')
        target_folders.append(target_dir + str(i) + '/')


for i in range(len(folders)):
    fd = folders[i]
    print(fd)
    tfd = target_folders[i]
    print(tfd)
    # rotation
    try:
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.rotate(probability=1, max_left_rotation=15, max_right_rotation=15)
        p.flip_left_right(probability=0.5)
        for i in range(10):
            p.process()
        del p
        # skew
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.skew(probability=1, magnitude=0.2)  # max 45 degrees
        p.flip_left_right(probability=0.5)
        for i in range(10):
            p.process()
        del p
        # shear
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.shear(probability=1, max_shear_left=10, max_shear_right=10)
        p.flip_left_right(probability=0.5)
        for i in range(10):
            p.process()
        del p
        # random_distortion
        #p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        #p.random_distortion(probability=1.0, grid_width=10, grid_height=10, magnitude=5)
        #p.flip_left_right(probability=0.5)
        #for i in range(10):
        #    p.process()
        #del p
    except Exception as exp:
        print(fd)
