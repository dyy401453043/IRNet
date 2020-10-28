import os
from subprocess import run

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

command = "python -u train.py --dataset ./data \
--glove_embed_path ./data/glove.1.300d.txt \
--cuda \
--epoch 50 \
--loss_epoch_threshold 50 \
--sketch_loss_coefficie 1.0 \
--beam_size 1 \
--seed 90 \
--save save_path \
--embed_size 300 \
--sentence_features \
--column_pointer \
--hidden_size 300 \
--lr_scheduler \
--lr_scheduler_gammar 0.5 \
--att_vec_size 300 "
          #"> save_path/log.txt"

run(command,shell=True)