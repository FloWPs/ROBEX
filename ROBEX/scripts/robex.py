################
##    ROBEX   ##
################

#---------------------
#  Import Librairies
#---------------------

import os, glob
import numpy as np
import nibabel as nib
from pyrobex.robex import robex

#----------------
#  Data Loading
#----------------

DATASET_PATH = 'data/'

SAVE_PATH = 'data/robex_data/'
im_dir = 'stripped_t1'
mask_dir = 'stripped_t1_mask'


SCANNER_LIST = ['Amsterdam_GE3T/GE3T/', 'Singapore/', 'Utrecht/']

for SCANNER in [SCANNER_LIST[0]]:#tqdm(SCANNER_LIST):

    print(f'[INFO] Scanner used: {SCANNER}\n')

    for d in ['100']: #glob.glob(os.path.join(DATASET_PATH,SCANNER,'*')):
        NUM = d.split('/')[-1]

        print('\n--------------------------------------------------------\n\nVolume from patient '+NUM)
        image_flair_pre = nib.load(DATASET_PATH + SCANNER + f'{NUM}/pre/FLAIR.nii.gz')
        image_T1_pre = nib.load(DATASET_PATH + SCANNER + f'{NUM}/pre/T1.nii.gz')
        # mask = nib.load(DATASET_PATH + SCANNER + f'{NUM}/wmh.nii.gz').get_fdata()
        print('[INFO] Files imported with sucess.')
        
        # strip brain with robex algorithm
        stripped_t1, mask = robex(image_T1_pre)

        os.makedirs(SAVE_PATH+im_dir+'/'+ NUM, exist_ok=True)
        os.makedirs(SAVE_PATH+mask_dir+'/'+ NUM, exist_ok=True)
        np.save(os.path.join(SAVE_PATH, im_dir, NUM, f'strip_brain_t1.npy'), stripped_t1.get_fdata())
        np.save(os.path.join(SAVE_PATH, mask_dir, NUM, f'strip_brain_t1_mask.npy'), mask.get_fdata())

        print('[INFO] Brains extracted with success.')
