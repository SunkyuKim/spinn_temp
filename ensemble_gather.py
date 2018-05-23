import os
import numpy as np
from sklearn import metrics

expstr = "DL_train4_ensemble_undersampling"
logits_symbol_list = []
logits_entire_list = []
logits_symbol_label=0
logits_entire_label=0
ckptnum = 4500
ckptnum = ""
for i in range(100):
    num = i+1

    #if not os.path.isfile("logs/%s_%s/logits_entire-%s"%(expstr, num, ckptnum)):
    if True:
        os.system("CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr=%s --logdir=logs/%s_%s --test_bool --ckptnum=%s"%(expstr, expstr, num, ckptnum))

    fr = open("logs/%s_%s/logits_entire-%s"%(expstr, num, ckptnum))
    logits_entire_list.append(np.array(eval(fr.readline())))
    logits_entire_label = np.array(eval(fr.readline()))
    fr.close()
    fr = open("logs/%s_%s/logits_symbol-%s"%(expstr, num, ckptnum))
    logits_symbol_list.append(np.array(eval(fr.readline())))
    logits_symbol_label = np.array(eval(fr.readline()))
    fr.close()


entire = np.mean(np.array(logits_entire_list),0)
symbol = np.mean(np.array(logits_symbol_list),0)
#entire = logits_entire_list[-1]

entire_f1 = metrics.f1_score(np.array(logits_entire_label), np.argmax(entire,1), average='micro')
symbol_f1 = metrics.f1_score(np.array(logits_symbol_label), np.argmax(symbol,1), average='micro')

print("entire:", entire_f1, "symbol:", symbol_f1)
