from __future__ import print_function
from argparse import ArgumentParser
import sys
sys.path.insert(0, 'src')
import os, random, subprocess, evaluate, shutil
from utils import exists, list_files
import pdb

TMP_DIR = '.fns_frames_%s/' % random.randint(0,99999)
DEVICE = '/gpu:0'
BATCH_SIZE = 4
BITRATE = '10000k'
PRESET = 'medium'

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--checkpoint', type=str,
                        dest='checkpoint', help='checkpoint directory or .ckpt file',
                        metavar='CHECKPOINT', required=True)

    parser.add_argument('--in-path', type=str,
                        dest='in_path', help='in video path',
                        metavar='IN_PATH', required=True)
    
    parser.add_argument('--out-path', type=str,
                        dest='out', help='path to save processed video to',
                        metavar='OUT', required=True)
    
    parser.add_argument('--tmp-dir', type=str, 
                        dest='tmp_dir', help='tmp dir for processing', 
                        metavar='TMP_DIR', default=TMP_DIR)

    parser.add_argument('--device', type=str, dest='device',
                        help='device for eval. CPU discouraged. ex: \'/gpu:0\'',
                        metavar='DEVICE', default=DEVICE)

    parser.add_argument('--batch-size', type=int,
                        dest='batch_size',help='batch size for eval. default 4.',
                        metavar='BATCH_SIZE', default=BATCH_SIZE)

    parser.add_argument('--no-disk', type=bool, 
                        dest='no_disk', help='Don\'t save intermediate files to disk. Default False',
                        metavar='NO_DISK', default=False)

    parser.add_argument('--bitrate', type=str, 
                        dest='bitrate', help='Bitrate of the output video. Default: 10000k', 
                        metavar='BITRATE', default=BITRATE, required=False)

    parser.add_argument('--preset', type=str, 
                        dest='preset', help='Encoding speed of compression ratio, slower means better compression. Possibilities are: ultrafast, superfast, veryfast, faster, fast, medium (default), slow, slower, veryslow, placebo', 
                        metavar='PRESET', default=PRESET, required=False)
    return parser

def check_opts(opts):
    exists(opts.checkpoint)
    exists(opts.out)

def main():
    parser = build_parser()
    opts = parser.parse_args()
    evaluate.ffwd_video(opts.bitrate, opts.preset, opts.in_path, opts.out, opts.checkpoint, opts.device, opts.batch_size)

 
if __name__ == '__main__':
    main()


