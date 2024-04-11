import os
import shutil

import torch
import torch.utils.data
import torchvision.transforms as transforms
import torchvision.datasets as datasets

import argparse

from helpers import makedir
import model
import push
import prune
import train_and_test as tnt
import save
from log import create_logger
from preprocess import mean, std, preprocess_input_function

model_ = torch.load('/home/hamed/PycharmProjects/CritProtoPNet/40nopush0.7491.pth',map_location='cuda')
print(model_)