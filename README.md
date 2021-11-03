# additional_openjtalk_dic

## ビルド方法
Ubuntu上でのビルドを想定しています。
```bash
$ sudo apt-get install -y --no-install-recommends \
        build-essential \
        gcc g++ cmake \
        unzip xz-utils \
      	libblas3 libblas-dev \
        mecab libmecab-dev swig \
        locales \
        nkf \
        python3-dev python3-pip python3-setuptools python3-tk

$ git clone --depth 1 --recursive --shallow-submodules https://github.com/takana-v/additional_openjtalk_dic
$ cd additional_openjtalk_dic
$ wget https://ccd.ninjal.ac.jp/unidic_archive/cwj/2.1.2/unidic-mecab_kana-accent-2.1.2_src.zip
$ unzip unidic-mecab_kana-accent-2.1.2_src.zip && cd unidic-mecab_kana-accent-2.1.2_src
$ ./configure && make
$ sudo make install && cd ../
$ find ./mecab-ipadic-neologd/seed/ -type f -name "*.xz" | xargs -I{} unxz -k {}
$ cat ./mecab-ipadic-neologd/seed/*.csv > neologd_all.csv
$ python3 -m pip install --upgrade pip && python3 -m pip install --upgrade setuptools
$ cd tdmelodic
$ python3 -m pip install -r requirements.txt
$ python3 -m pip install .
$ cd ../
$ python3 main.py
```
最後の行でかなり時間が掛かると思います。  
PCによりますが下手すると数日かかるかもしれません。  
手元の環境ではneologd_all.csvが5572307行あったので50行/秒で処理するとすると31時間ほどかかります。  
additional_openjtalk_dic.csvが完成した辞書ファイルです。  
