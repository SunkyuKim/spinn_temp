import os
import pandas as pd

mainfile = open("genefusion-data/snli-dl-version/processed_train4-1_unique_id_180521_lim_result_pre.tsv",encoding='utf8').readlines()
mainfile_dict = dict()

for l in open("genefusion-data/DL_uniqueid/[id]processed_train4-1_unique_id_180521_lim_result_pre.tsv", encoding='utf8'):
    tokens = l.strip().split("\t")
    mainfile_dict[tokens[0]] = int(tokens[1])

emb_name = "ensemble_index_180523/"
#emb_name = "yuanfang_undersample_indexes/"
save_name = "dl_4-1_oversampling/"
target_dir = "genefusion-data/snli-dl-version/%s"%save_name
if not os.path.isdir(target_dir):
    os.mkdir(target_dir)

for i in range(10):
    idx_ = i+1
    ids = open("/mnt/smb/Q/sunkyu/gpower4/%s/train4-1_%s_index.txt"%(emb_name,idx_)).readlines()

    indices = [mainfile_dict[v.strip()] for v in ids]

    with open(target_dir+str(idx_)+".tsv", "w", encoding="utf8") as fw:
        for j in indices:
            fw.write(mainfile[j])

idx_ = "val"
ids = open("/mnt/smb/Q/sunkyu/gpower4/%s/train4-1_%s_index.txt"%(emb_name,idx_)).readlines()

indices = [mainfile_dict[v.strip()] for v in ids]

with open(target_dir+str(idx_)+".tsv", "w", encoding="utf8") as fw:
    for j in indices:
        fw.write(mainfile[j])

