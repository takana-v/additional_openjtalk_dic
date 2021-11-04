from tdmelodic.filters.neologd_preprocess import Preprocess
from tdmelodic.filters.neologd_patch import NeologdPatch

with open("neologd_all.csv", encoding="utf-8", newline="") as f:
    with open("neologd_omitted.csv", encoding="utf-8", newline="", mode="w") as f2:
        preprocess = Preprocess(False, NeologdPatch(**{"input":"neologd_all.csv","output":"neologd_omitted.csv","mode":"ipadic","rm_hashtag":True,"rm_noisy_katakana":True,"rm_person":False,"rm_emoji":False,"rm_symbol":False,"rm_numeral":False,"rm_wrong_yomi":True,"rm_special_particle":True,"cor_longvow":True,"cor_yomi_num":True,"normalize":False}),"ipadic")
        preprocess(f, f2)
