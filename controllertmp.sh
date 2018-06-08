
CUDA_VISIBLE_DEVICES=0 python spinn_chemprot.py --genefusion_expstr=DL_train4 --logdir=logs/DL_train4_10tmp --epochs=25
CUDA_VISIBLE_DEVICES= python spinn_chemprot.py --genefusion_expstr=DL_train4 --logdir=logs/DL_train4_10tmp --test_bool
