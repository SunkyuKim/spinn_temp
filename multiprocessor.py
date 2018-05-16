import os
from multiprocessing import Pool

def foo(x):
    expstr = "DL_train4_gs"

    expnum = x+1

    cmdstr = \
    "CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr={expstr} --logdir=logs/{expstr}_{expnum} --epochs=25 && "\
    "CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr={expstr} --logdir=logs/{expstr}_{expnum} --test_bool".format(expstr=expstr, expnum=expnum)
    print(cmdstr)
    os.system(cmdstr)

if __name__ == '__main__':
    p = Pool(3)
    p.map(foo, range(10))

