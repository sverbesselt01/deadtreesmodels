For the inference on an orthophoto adjust `infer_ortho.py`. 

Model weights: https://data2.deadtrees.earth/assets/v1/segformer_b5_full_epoch_100.safetensors

Tree cover (https://restor-foundation.github.io/tcd/dataset/) is not running atm. 

Questions: clemens.mosig@uni-leipzig.de

## Adaptations:
* slight modifications of the infer_ortho.py and tileinference.py so it works on a windows computer. I did inference with the segformer-unet and used the pre-trained weights that are in the link above.

### Extra information:
I used python 3.10.
