sudo apt -y install kaggle 
mkdir <your base dir>
cd <your base dir>
export KAGGLE_USERNAME=<your kaggle username>
export KAGGLE_KEY=<your kaggle key>

# stanford cars dataset (ref: https://github.com/pytorch/vision/issues/7545#issuecomment-1631441616)
mkdir stanford_cars && cd stanford_cars
kaggle datasets download -d jessicali9530/stanford-cars-dataset
kaggle datasets download -d abdelrahmant11/standford-cars-dataset-meta
unzip standford-cars-dataset-meta.zip
unzip stanford-cars-dataset.zip
tar -xvzf car_devkit.tgz
mv cars_test a
mv a/cars_test/ cars_test
rm -rf a
mv cars_train a
mv a/cars_train/ cars_train
rm -rf a
mv 'cars_test_annos_withlabels (1).mat' cars_test_annos_withlabels.mat
rm -rf 'cars_annos (2).mat' *.zip
cd ..

# ressic45
mkdir resisc45 && cd resisc45
# (manual download) https://onedrive.live.com/?authkey=%21AHHNaHIlzp%5FIXjs&id=5C5E061130630A68%21107&cid=5C5E061130630A68&parId=root&parQt=sharedby&o=OneUp
mv ~/NWPU-RESISC45.rar ./
sudo apt -y install unar
unar NWPU-RESISC45.rar
wget -O resisc45-train.txt "https://storage.googleapis.com/remote_sensing_representations/resisc45-train.txt"
wget -O resisc45-val.txt "https://storage.googleapis.com/remote_sensing_representations/resisc45-val.txt"
wget -O resisc45-test.txt "https://storage.googleapis.com/remote_sensing_representations/resisc45-test.txt"
rm -rf NWPU-RESISC45.rar
cd ..

# dtd
mkdir dtd && cd dtd
wget https://www.robots.ox.ac.uk/~vgg/data/dtd/download/dtd-r1.0.1.tar.gz
tar -xvzf dtd-r1.0.1.tar.gz
rm -rf dtd-r1.0.1.tar.gz
mv dtd/images images
mv dtd/imdb/ imdb
mv dtd/labels labels
cat labels/train1.txt labels/val1.txt > labels/train.txt
cat labels/test1.txt > labels/test.txt

# euro_sat
mkdir euro_sat && cd euro_sat
wget --no-check-certificate https://madm.dfki.de/files/sentinel/EuroSAT.zip
unzip EuroSAT.zip
rm -rf EuroSAT.zip

# sun397
mkdir sun397 && cd sun397
wget http://vision.princeton.edu/projects/2010/SUN/SUN397.tar.gz
unzip Partitions.zip
tar -xvzf SUN397.tar.gz
rm -rf SUN397.tar.gz
