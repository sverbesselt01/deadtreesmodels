from deadwood.deadwood_inference import DeadwoodInference
import rasterio
from common.common import *

#filename = "/scratch/cmosig/test_image_seg/20211001_FVA_Walddrohnen_Totholz_3_ortho.tif"
#filename = "C:/Users/sebastiaan_verbessel/Downloads/tile.tif"
#filename = "C:/Users/sebastiaan_verbessel/Downloads/target_tif.tif"

filename = "C:/Users/sebastiaan_verbessel/Downloads/Ortho_BTR.tif"


deadwodinference = DeadwoodInference(config_path="deadwood_inference_config.json")
polygons = deadwodinference.inference_deadwood(filename)
save_poly("deadwood_test.gpkg", polygons, crs=rasterio.open(filename).crs)
