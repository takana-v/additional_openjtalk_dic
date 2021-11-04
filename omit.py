import csv
import re

from tqdm import tqdm
from tdmelodic.nn.convert import Converter
from tdmelodic.filters.neologd_preprocess import Preprocess
from tdmelodic.filters.neologd_patch import NeologdPatch

with open("neologd_all.csv", encoding="utf-8", newline="") as f:
    with open("neologd_omitted.csv", encoding="utf-8", newline="", mode="w") as f2:
        preprocess = Preprocess(True, NeologdPatch(**{"input":"neologd_all.csv","output":"neologd_omitted.csv","mode":"ipadic","rm_hashtag":True,"rm_noisy_katakana":True,"rm_person":False,"rm_emoji":False,"rm_symbol":False,"rm_numeral":False,"rm_wrong_yomi":True,"rm_special_particle":True,"cor_longvow":True,"cor_yomi_num":True,"normalize":False}),"ipadic")
        preprocess(f, f2)

converter = Converter()
prog = re.compile('(?:[アイウエオカ-モヤユヨ-ロワ-ヶ][ァィゥェォャュョヮ]|[アイウエオカ-モヤユヨ-ロワ-ヶー])')
with open("neologd_omitted.csv", newline="", encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    with open("additional_openjtalk_omitted_dic.csv", mode="w",newline="", encoding="utf-8") as f2:
        csv_writer = csv.writer(f2)
        for l in tqdm(csv_reader):
            add_l = l[0:13]
            add_l.append(f"{converter.sy2a(l[0],l[12]).find('[')+1}/{len(prog.findall(l[12]))}")
            add_l.append("*")
            csv_writer.writerow(add_l)
