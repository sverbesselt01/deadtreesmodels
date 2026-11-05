import sys
import segmentation_models_pytorch as smp
from torchvision.transforms import transforms
import torch
from torch.utils.data import DataLoader
#from unet_model import UNet
from torchvision.transforms.functional import crop
import os

import geopandas as gpd
import numpy as np
import rasterio
import utm
from safetensors.torch import load_model
from shapely.affinity import affine_transform, translate
from shapely.geometry import Polygon, MultiPolygon

# DEADWOOD_MODEL_PATH = "/net/scratch/cmosig/model.safetensors"
# DEADWOOD_MODEL_PATH = "/net/scratch/jmoehring/checkpoints/3d_18k_100e_vanilla_tversky_a01b09g2/fold_0_epoch_99/model.safetensors"
#DEADWOOD_MODEL_PATH = "/net/scratch/cmosig/experiment_dir_deadwood_segmentation/segformer_b5_oversample_newdata/fold_0_epoch_74/model.safetensors"
DEADWOOD_MODEL_PATH = "model/segformer_b5_full_epoch_100.safetensors"

# pathtotile = sys.argv[1]    
#pathtotile = "/net/scratch/jmoehring/tiles/spain_20_09_2023_south_tejeda_1_ortho/0.08/1588_4484.tif"
pathtotile = "C:/Users/sebastiaan_verbessel/Downloads/tile.tif"
# pathtotile = "/net/scratch/jmoehring/tiles/spain_20_09_2023_south_tejeda_1_ortho/0.08/1588_900.tif"

# preferably use GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# load image patch 
image = None
with rasterio.open(pathtotile) as src:
    # Read only bands 1, 2, and 3 (RGB) # Forth band is the alpha band # image = src.read()
    image = src.read([1, 2, 3])


    # Reshape the image tensor to have 3 channels
    image = image.transpose(1, 2, 0)

    # # If the raster data is uint16 or needs scaling to [0, 1]:
    print(image.dtype)