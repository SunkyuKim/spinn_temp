import os
import pandas as pd


trainfile_code = "4"
#trainfile_code = "4-1"

#mainfile = open("genefusion-data/snli-dl-version/processed_train" + trainfile_code + "_unique_id_180521_lim_result_pre.tsv",encoding='utf8').readlines()
mainfile = open("genefusion-data/snli-dl-version/dl_train" + trainfile_code + "_unique_id_lim_result_pre.tsv",encoding='utf8').readlines()
mainfile_dict = dict()

#for l in open("genefusion-data/DL_uniqueid/[id]processed_train" + trainfile_code + "_unique_id_180521_lim_result_pre.tsv", encoding='utf8'):
for l in open("genefusion-data/DL_uniqueid/[id]dl_train" + trainfile_code + "_unique_id_lim_result_pre.tsv", encoding='utf8'):
    tokens = l.strip().split("\t")
    mainfile_dict[tokens[0]] = int(tokens[1])

#emb_name = "ensemble_index_180523/"
#emb_name = "yuanfang_undersample_100/"
emb_name = "yuanfang_undersample_300/"
#emb_name = "yuanfang_undersample_indexes/"
#save_name = "dl_" + trainfile_code + "_oversampling/"
save_name = "dl_" + trainfile_code + "_undersampling_300/"
target_dir = "genefusion-data/snli-dl-version/%s"%save_name
if not os.path.isdir(target_dir):
    os.mkdir(target_dir)

for i in range(300):
    idx_ = i+1
    ids = open("/mnt/smb/Q/sunkyu/gpower4/%s/train%s_%s_index.txt"%(emb_name,trainfile_code,idx_)).readlines()

    indices = [mainfile_dict[v.strip()] for v in ids]

    with open(target_dir+str(idx_)+".tsv", "w", encoding="utf8") as fw:
        for j in indices:
            fw.write(mainfile[j])

idx_ = "val"
ids = open("/mnt/smb/Q/sunkyu/gpower4/%s/train%s_%s_index.txt"%(emb_name,trainfile_code, idx_)).readlines()

indices = [mainfile_dict[v.strip()] for v in ids]

with open(target_dir+str(idx_)+".tsv", "w", encoding="utf8") as fw:
    for j in indices:
        fw.write(mainfile[j])

