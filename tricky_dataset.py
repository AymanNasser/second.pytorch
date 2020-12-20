import os
import shutil
desired_path = '/home/ayman/FOE-Linux/Graduation_Project/second.pytorch/second/data/ImageSets/KITTI_DATASET_ROOT'

training_path = '/training/image_2'
testing_path = '/testing/image_2'

training_ids = 7841
testing_ids = 7518

path = desired_path + testing_path
os.chdir(path)

for i in range(testing_ids):

    shutil.copy(desired_path + '/000000.png', path)
    fill_no = 6 - len(str(i))
    empt_str = ""
    os.rename('000000.png', str(empt_str.ljust(fill_no, '0') + str(i) + '.png'))
    print(i," Succ.")


