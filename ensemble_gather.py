import os
import numpy as np
from sklearn import metrics
import getpass


expstr = "DL_train4"
#expstr = "DL_train4_ensemble_oversampling"
#expstr = "DL_train4-1_ensemble_oversampling"
#expstr = "DL_train4-1_ensemble_undersampling"
#expstr = "DL_train4-1_ensemble_undersampling_300"
logits_symbol_list = []
logits_nonsymbol_list = []
logits_entire_list = []
logits_nonsymbol_label=0
logits_symbol_label=0
logits_entire_label=0
ckptnum = "4500"


logdir = "logs/"
if getpass.getuser() != "sunkyu":
    logdir = "/mnt/disks/ssd/spinn/logs/"
else:
    logdir = "logs/"


for i in range(10):
    num = i+1

    if not os.path.isfile("%s/%s-%s/logits_nonsymbol-%s"%(logdir, expstr, num, ckptnum)):
    #if True:
        os.system("CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr=%s --logdir=%s/%s-%s --test_bool --ckptnum=%s"%(expstr, logdir, expstr, num, ckptnum))

    fr = open("%s/%s-%s/logits_entire-%s"%(logdir, expstr, num, ckptnum))
    logits_entire_list.append(np.array(eval(fr.readline())))
    logits_entire_label = np.array(eval(fr.readline()))
    fr.close()
    fr = open("%s/%s-%s/logits_symbol-%s"%(logdir, expstr, num, ckptnum))
    logits_symbol_list.append(np.array(eval(fr.readline())))
    logits_symbol_label = np.array(eval(fr.readline()))
    fr.close()
    fr = open("%s/%s-%s/logits_nonsymbol-%s"%(logdir, expstr, num, ckptnum))
    logits_nonsymbol_list.append(np.array(eval(fr.readline())))
    logits_nonsymbol_label = np.array(eval(fr.readline()))
    fr.close()


entire = np.mean(np.array(logits_entire_list),0)
symbol = np.mean(np.array(logits_symbol_list),0)
nonsymbol = np.mean(np.array(logits_nonsymbol_list),0)
#entire = logits_entire_list[-1]

entire_f1 = metrics.f1_score(np.array(logits_entire_label), np.argmax(entire,1), average='micro')
symbol_f1 = metrics.f1_score(np.array(logits_symbol_label), np.argmax(symbol,1), average='micro')
nonsymbol_f1 = metrics.f1_score(np.array(logits_nonsymbol_label), np.argmax(nonsymbol,1), average='micro')

print("entire:", entire_f1, "symbol:", symbol_f1, "nonsymbol:", nonsymbol_f1)
