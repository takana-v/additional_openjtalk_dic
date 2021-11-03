import csv
import re

from tqdm import tqdm
from tdmelodic.nn.convert import Converter

converter = Converter()
prog = re.compile('(?:[アイウエオカ-モヤユヨ-ロワ-ヶ][ァィゥェォャュョヮ]|[アイウエオカ-モヤユヨ-ロワ-ヶー])')
with open("neologd_all.csv", newline="", encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    with open("additional_openjtalk_dic.csv", mode="w",newline="", encoding="utf-8") as f2:
        csv_writer = csv.writer(f2)
        for l in tqdm(csv_reader):
            add_l = l[0:13]
            add_l.append(f"{converter.sy2a(l[0],l[12]).find('[')+1}/{len(prog.findall(l[12]))}")
            add_l.append("*")
            csv_writer.writerow(add_l)