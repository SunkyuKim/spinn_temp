import os

mainfile = open("genefusion-data/snli-dl-version/dl_train4_unique_id_lim_result_pre.tsv",encoding='utf8').readlines()
mainfile_dict = dict()
for l in open("genefusion-data/DL_uniqueid/[id]dl_train4_unique_id_lim_result_pre.txt"):
    tokens = l.strip().split("\t")
    mainfile_dict[tokens[0]] = int(tokens[1])


#emb_name = "ensemble_index_180515/"
emb_name = "yuanfang_undersample_indexes/"
target_dir = "genefusion-data/snli-dl-version/%s"%emb_name
if not os.path.isdir(target_dir):
    os.mkdir(target_dir)

for i in range(100):
    idx_ = i+1
    ids = open("/mnt/smb/Q/sunkyu/gpower4/%s/train4_%s_index.txt"%(emb_name,idx_)).readlines()

    indices = [mainfile_dict[v.strip()] for v in ids]

    with open(target_dir+str(idx_)+".tsv", "w", encoding="utf8") as fw:
        for j in indices:
            fw.write(mainfile[j])

idx_ = "val"
ids = open("/mnt/smb/Q/sunkyu/gpower4/%s/train4_%s_index.txt"%(emb_name,idx_)).readlines()

indices = [mainfile_dict[v.strip()] for v in ids]

with open(target_dir+str(idx_)+".tsv", "w", encoding="utf8") as fw:
    for j in indices:
        fw.write(mainfile[j])

