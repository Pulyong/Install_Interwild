import cv2
import numpy as np
import glob
import os

# 체스보드 설정
numCornersHor = 7  # 체스보드 가로 코너 수
numCornersVer = 4  # 체스보드 세로 코너 수

def chessBoard(path):
    obj = np.zeros((1,numCornersHor * numCornersVer, 3), np.float32)
    obj[0,:, :2] = np.mgrid[0:numCornersHor, 0:numCornersVer].T.reshape(-1, 2)

    objectPoints = []
    imagePoints = []

    images = glob.glob(path)

    for imagePath in images:
        image = cv2.imread(imagePath)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        found, corners = cv2.findChessboardCorners(grayImage, (numCornersHor, numCornersVer))

        if found:
            cv2.cornerSubPix(grayImage, corners, (11, 11), (-1, -1),
                             (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1))
            imagePoints.append(corners)
            objectPoints.append(obj)

            cv2.drawChessboardCorners(image, (numCornersHor, numCornersVer), corners, found)
            cv2.imshow("Corners on Chessboard", image)
            cv2.waitKey(100)

    cv2.destroyAllWindows()
    flags = cv2.fisheye.CALIB_RECOMPUTE_EXTRINSIC | cv2.fisheye.CALIB_CHECK_COND | cv2.fisheye.CALIB_FIX_SKEW
    rms, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.fisheye.calibrate(
        objectPoints, imagePoints, grayImage.shape[::-1], None, None,flags=flags
    )

    print("Camera Matrix:\n", cameraMatrix)
    print("Distortion Coefficients:\n", distCoeffs)


def main():
    imagePath = '/home/shu/Desktop/Yongjin/hands/dataset/Fisheye/calibration/chessboard/*'
    chessBoard(imagePath)

if __name__ == "__main__":
    main()