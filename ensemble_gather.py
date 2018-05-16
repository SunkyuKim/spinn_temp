import os
import numpy as np
from sklearn import metrics

logits_symbol_list = []
logits_entire_list = []
logits_symbol_label=0
logits_entire_label=0
ckptnum = 4500
for i in range(8):
    num = i+1

    if not os.path.isfile("logs/DL_train4_%s/logits_entire-%s"%(num, ckptnum)):
    #if True:
        os.system("CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr=DL_train4 --logdir=logs/DL_train4_%s --test_bool --ckptnum=%s"%(num, ckptnum))

    fr = open("logs/DL_train4_%s/logits_entire-%s"%(num, ckptnum))
    logits_entire_list.append(np.array(eval(fr.readline())))
    logits_entire_label = np.array(eval(fr.readline()))
    fr.close()
    fr = open("logs/DL_train4_%s/logits_symbol-%s"%(num, ckptnum))
    logits_symbol_list.append(np.array(eval(fr.readline())))
    logits_symbol_label = np.array(eval(fr.readline()))
    fr.close()


entire = np.mean(np.array(logits_entire_list),0)
symbol = np.mean(np.array(logits_symbol_list),0)
#entire = logits_entire_list[-1]

entire_f1 = metrics.f1_score(np.array(logits_entire_label), np.argmax(entire,1), average='micro')
symbol_f1 = metrics.f1_score(np.array(logits_symbol_label), np.argmax(symbol,1), average='micro')

print(entire_f1, symbol_f1)
