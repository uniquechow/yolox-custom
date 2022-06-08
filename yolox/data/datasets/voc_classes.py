#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
from pathlib import Path
import os
# VOC_CLASSES = ( '__background__', # always index 0
from yolox.data import get_yolox_datadir
from datasets.datacfg import cn

# 注意：最后一个类别后面也要加上 ,

VOC_CLASSES = tuple(cn)
text1 = 1

# VOC_CLASSES = (
#     "aeroplane",
#     "bicycle",
#     "bird",
#     "boat",
#     "bottle",
#     "bus",
#     "car",
#     "cat",
#     "chair",
#     "cow",
#     "diningtable",
#     "dog",
#     "horse",
#     "motorbike",
#     "person",
#     "pottedplant",
#     "sheep",
#     "sofa",
#     "train",
#     "tvmonitor",
# )
