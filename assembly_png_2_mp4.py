from subprocess import call
import subprocess
import os
import os.path as osp
from multiprocessing.dummy import Pool as ThreadPool


def process(folder):
    save_path = osp.join(submit, osp.basename(folder)) + '.mp4'
    cmd_coder = f'ffmpeg -i {folder}/%4d.png -vcodec libx265 -pix_fmt yuv422p -crf 10 {save_path}'
    process_yuv = subprocess.Popen(cmd_coder, shell=True)
    process_yuv.wait()

if __name__ == '__main__':
    #### change here
    sourcedir = '/data4/zjz_temp/datasets/SDR4K/val/result'
    submit = '/data4/zjz_temp/datasets/SDR4K/val/submit'
    ####
    os.makedirs(submit, exist_ok=True)
    folders = [osp.join(sourcedir, f) for f in os.listdir(sourcedir)]
    pool = ThreadPool()
    pool.map(process, folders)
    pool.close()
    pool.join()

