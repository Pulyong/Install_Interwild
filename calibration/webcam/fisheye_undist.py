import cv2
import numpy as np
import os
import glob

DIM=(800, 600)
K=np.array([[304.644177425368, 0.0, 398.44343443431563], [0.0, 303.81637854769906, 307.78390837256484], [0.0, 0.0, 1.0]])
D=np.array([[-0.048625006015903686], [0.0059879046129073564], [-0.04620707563307452], [0.05588028929371777]])

def fisheye_undistort(image, balance=0.0, dim2=None, dim3=None):
    dim1 = image.shape[:2][::-1] 

    assert dim1[0]/dim1[1] == DIM[0]/DIM[1]
    if not dim2:
        dim2 = dim1
    if not dim3:
        dim3 = dim1
    scaled_K = K * dim1[0] / DIM[0] 
    scaled_K[2][2] = 1.0 
    new_K = cv2.fisheye.estimateNewCameraMatrixForUndistortRectify(scaled_K, 
   									 D,dim2, np.eye(3), balance=balance)
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(scaled_K, D, 
    									np.eye(3), new_K,dim3, cv2.CV_16SC2)
    undistorted_img = cv2.remap(image, map1, map2,
    				interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
                    
    return undistorted_img
