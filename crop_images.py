import cv2
import os
import shutil
dataset_base_dir = '/home/hamed/project_antwerp/dataset/CUB_200_2011/CUB_200_2011/images/'
bounding_boxes_info = open("/home/hamed/project_antwerp/dataset/CUB_200_2011/CUB_200_2011/bounding_boxes.txt", "r")
images_dir = open("/home/hamed/project_antwerp/dataset/CUB_200_2011/CUB_200_2011/images.txt", "r")
classes_info = open("/home/hamed/project_antwerp/dataset/CUB_200_2011/CUB_200_2011/classes.txt", "r")
image_class_labels_info = open("/home/hamed/project_antwerp/dataset/CUB_200_2011/CUB_200_2011/image_class_labels.txt", "r")
train_test_info = open("/home/hamed/project_antwerp/dataset/CUB_200_2011/CUB_200_2011/train_test_split.txt","r")

train_croped_basedir = '/home/hamed/project_antwerp/dataset/CUB_200_2011/train_cropped/'
train_dir = '/home/hamed/project_antwerp/dataset/CUB_200_2011/train/'
test_croped_basedir = '/home/hamed/project_antwerp/dataset/CUB_200_2011/test_cropped/'
test_dir = '/home/hamed/project_antwerp/dataset/CUB_200_2011/test/'

bounding_boxes_lines = bounding_boxes_info.read().split('\n')
bounding_boxes_dic = {}
for line in bounding_boxes_lines:
    temp = line.split(' ')
    if len(temp) < 2:
        break
    bounding_boxes_dic[temp[0]] = temp[1:5]

images_dir_lines = images_dir.read().split('\n')
images_dir_dic = {}
for line in images_dir_lines:
    temp = line.split(' ')
    if len(temp) < 2 :
        break
    images_dir_dic[temp[0]] = temp[1]

itrain_test_lines = train_test_info.read().split('\n')
train_test_dic = {}
for line in itrain_test_lines:
    temp = line.split(' ')
    if len(temp) < 2 :
        break
    train_test_dic[temp[0]] = temp[1]

image_class_labels_lines = image_class_labels_info.read().split('\n')
image_class_labels_dic = {}
for line in image_class_labels_lines:
    temp = line.split(' ')
    if len(temp) < 2 :
        break
    image_class_labels_dic[temp[0]] = temp[1]


image_ids =  bounding_boxes_dic.keys()
for image_id in image_ids:
    image = cv2.imread(dataset_base_dir + images_dir_dic[image_id], 1)
    annot = [int(float(pixel_num)) for pixel_num in bounding_boxes_dic[image_id]]
    image_crop = image[annot[1]:annot[1]+annot[3], annot[0]:annot[0] + annot[2],:]
    class_id = image_class_labels_dic [image_id]
    class_id = int(class_id) - 1
    if class_id < 10:
        class_id = '00'+str(class_id)
    elif class_id < 100:
        class_id = '0'+str(class_id)
    else:
        class_id = str(class_id)
    image_name = images_dir_dic[image_id].split('/')[-1]
    if train_test_dic[image_id] == '1': # this is a tain image
        if not os.path.exists(train_croped_basedir+class_id):
            os.makedirs(train_croped_basedir+class_id)
            os.makedirs(train_dir+class_id)
        cv2.imwrite(train_croped_basedir+class_id+'/'+image_name, image_crop)
        shutil.copy(dataset_base_dir + images_dir_dic[image_id], train_dir+class_id+'/')
    else: # this is a test image
        if os.path.exists(test_croped_basedir+class_id) != True:
            os.makedirs(test_croped_basedir+class_id)
            os.makedirs(test_dir+class_id)
        cv2.imwrite(test_croped_basedir+class_id+'/'+image_name, image_crop)
        shutil.copy(dataset_base_dir + images_dir_dic[image_id], test_dir + class_id)
        pass


