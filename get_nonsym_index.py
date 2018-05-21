import configparser


path = configparser.ConfigParser()
path.read("exp_paths.ini")

ent = [v.strip() for v in open("genefusion-data/DL version/dl_test_lim_result_pre.tsv", encoding="utf-8").readlines()]
sym = [v.strip() for v in open("genefusion-data/DL version/dl_test_os_lim_result_pre.tsv", encoding="utf-8").readlines()]

indexdict = dict()
for i,l in enumerate(ent):
    indexdict[l] = i

symindex = [indexdict[v] for v in sym if v in indexdict]
print(symindex)
