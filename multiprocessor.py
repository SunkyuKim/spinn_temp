import os
from multiprocessing import Pool

def foo(x):
    #expstr = "DL_train4_gs"
    #expstr = "DL_train4-1_ensemble_oversampling"
    #expstr = "DL_train4-1_ensemble_undersampling"
    expstr = "DL_train4-1_ensemble_undersampling_300"


    expnum = x+1

    cmdstr = \
    "CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr={expstr} --logdir=/mnt/disks/ssd/spinn/logs/{expstr}-{expnum} --epochs=20 --ensemble_num={expnum} && "\
    "CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr={expstr} --logdir=/mnt/disks/ssd/spinn/logs/{expstr}-{expnum} --test_bool".format(expstr=expstr, expnum=expnum)
    print(cmdstr)
    os.system(cmdstr)

if __name__ == '__main__':
    p = Pool(20)
    p.map(foo, range(300))

