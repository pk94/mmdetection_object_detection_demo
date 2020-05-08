from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET
from PIL import Image

def train_test_split(files, files_path, test=0.1):
    split = int(len(files) * test)
    test = files[:split]
    train = files[split:]
    with open(f'{files_path}\\test.txt', 'w') as f1:
        for line in test:
            f1.write(f'{line[:-4]}\n')
    f1.close()
    with open(f'{files_path}\\train.txt', 'w') as f1:
        for line in train:
            f1.write(f'{line[:-4]}\n')
    f1.close()

def png_to_jpg(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        im1 = Image.open(f'{path}\\{file}')
        im1.save(f'{path}2\{file[:-3]}jpg')


dataset_path = r'..\data\VOC2007\JPEGImages'
ann_save_path = r'..\data\VOC2007\Annotations\\'
train_test_path = r'..\data\VOC2007\ImageSets'

files = [f for f in listdir(dataset_path) if isfile(join(dataset_path, f))]
tree = ET.parse('template.xml')
root = tree.getroot()

# png_to_jpg(dataset_path)

for file in files:
    for filename in root.iter('filename'):
        filename.text = file
    for path in root.iter('path'):
        path.text = dataset_path + '\\' + file
    tree.write(f'{ann_save_path}{file[:-3]}xml')

train_test_split(files, train_test_path)


