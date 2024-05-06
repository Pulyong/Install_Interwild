import numpy as np
import cv2
import glob

camera_matrix = np.array([[304.644177425368, 0.0, 398.44343443431563], [0.0, 303.81637854769906, 307.78390837256484], [0.0, 0.0, 1.0]])

dist_coeffs = np.array([[-0.048625006015903686], [0.0059879046129073564], [-0.04620707563307452], [0.05588028929371777]])

fx, fy = camera_matrix[0,0], camera_matrix[1,1]
cx, cy = camera_matrix[0,2], camera_matrix[1,2]
k1,k2,k3 = dist_coeffs[:3,0]

def undistortImage(inputImg, type=1):
    height, width = inputImg.shape[:2]

    undistortedImg = np.zeros_like(inputImg)

    # Generate grid of pixel coordinates
    j_coords, i_coords = np.meshgrid(np.arange(width), np.arange(height))
    
    # Calculate normalized coordinates
    x = (j_coords - cx) / fx
    y = (i_coords - cy) / fy
    r = np.sqrt(x ** 2 + y ** 2)

    # Calculate distorted radius
    if type == 1:
        theta = np.arctan(r)
    else:
        theta = r
    theta_d = theta * (1 + k1 * theta ** 2 + k2 * theta ** 4 + k3 * theta ** 6)

    # Calculate distorted coordinates
    xDistorted = x / r * theta_d
    yDistorted = y / r * theta_d 

    # Map distorted coordinates back to image plane
    u = np.round(fx * xDistorted + cx).astype(int)
    v = np.round(fy * yDistorted + cy).astype(int)

    # Ensure indices are within bounds
    u = np.clip(u, 0, width - 1)
    v = np.clip(v, 0, height - 1)

    # Undistort image
    undistortedImg = inputImg[v, u]
    return undistortedImg

def main():
    imgPath = glob.glob('/home/shu/Desktop/Yongjin/hands/dataset/Fisheye/calibration/chessboard/*')
    for img in imgPath:
        image = cv2.imread(img)
        undistortImage(image,1)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()