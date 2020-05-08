from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

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


dataset_path = r'C:\Pawel\Datasets\planes\Images'
ann_save_path = r'C:\Pawel\Datasets\planes\Annotations\\'
train_test_path = r'C:\Pawel\Datasets\planes\ImagesSets'

files = [f for f in listdir(dataset_path) if isfile(join(dataset_path, f))]
tree = ET.parse('template.xml')
root = tree.getroot()

for file in files:
    for filename in root.iter('filename'):
        filename.text = file
    for path in root.iter('path'):
        path.text = dataset_path + '\\' + file
    tree.write(f'{ann_save_path}{file[:-3]}xml')

train_test_split(files, train_test_path)


