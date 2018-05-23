import os
from multiprocessing import Pool

def foo(x):
    #expstr = "DL_train4_gs"
    expstr = "DL_train4_ensemble_undersampling"


    expnum = x+1

    cmdstr = \
    "CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr={expstr} --logdir=logs/{expstr}_{expnum} --epochs=50 --ensemble_num={expnum} --save_every=300 && "\
    "CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr={expstr} --logdir=logs/{expstr}_{expnum} --test_bool".format(expstr=expstr, expnum=expnum)
    print(cmdstr)
    os.system(cmdstr)

if __name__ == '__main__':
    p = Pool(10)
    p.map(foo, range(100))

