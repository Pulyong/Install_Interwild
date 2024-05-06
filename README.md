# Install_Interwild

[Interwild](https://github.com/facebookresearch/InterWild) 논문의 구현 모델을 설치하고 Fisheye camera로 Webcam demo를 돌리기 위한 레포입니다.

## Requirements
```
1.
conda create -n interwild python=3.9 -y
conda activate interwild

2.
##################################
# conda install pytorch >= 2.0.1 #
##################################

3.
# pytorch 3d 설치 시작

conda install -c fvcore -c iopath -c conda-forge fvcore iopath

#####################################################
For the CUB build time dependency, which you only need if you have CUDA older than 11.7, if you are using conda, you can continue with

conda install -c bottler nvidiacub

Otherwise download the CUB library from https://github.com/NVIDIA/cub/releases and unpack it to a folder of your choice. Define the environment variable CUB_HOME before building and point it to the directory that contains CMakeLists.txt for CUB. For example on Linux/Mac,

curl -LO https://github.com/NVIDIA/cub/archive/1.10.0.tar.gz
tar xzf 1.10.0.tar.gz
export CUB_HOME=$PWD/cub-1.10.0
#####################################################

conda install pytorch3d -c pytorch3d

# pytorch 3d 설치 끝

4.
conda install --yes --file conda_requirements.txt
pip install -r requirements.txt
```
[Pytorch](https://pytorch.org/get-started/previous-versions/) >= 2.0.1가 필요합니다.  

## Demo
1. [Interwild](https://github.com/facebookresearch/InterWild) 를 Clone 받습니다.
2. 'Install_Interwild_directory/interwild'의 fisheye_undist.py,fisheye_webcam.py 파일을 'InterWild_directory/demo'에 위치시킵니다.
3. [Demo 링크](https://github.com/facebookresearch/InterWild?tab=readme-ov-file#demo)에서 Model weight를 다운로드 하거나, [Test 링크](https://github.com/facebookresearch/InterWild?tab=readme-ov-file#test)에서 여러 Dataset으로 Pretrained된 weight를 다운로드 합니다.
4. 다운로드한 Weight를 'InterWild_Directory/demo'에 위치시킵니다.
5. 'InterWild_Directory/demo'로 이동합니다.
6. ```python fisheye_webcam.py --gpu 0```으로 실행합니다.

## Directory
### Install_Interwild Directory
```
Install_Interwild
├── calibration
│   ├── calibration
│   │   ├── calibration.py
│   │   ├── fisheye_calib.py
│   │   └── save_chessboard.py
│   └── webcam
│       ├── fisheye_undist.py
│       ├── test_fisheye.py
│       ├── test_undist.py
│       └── undistortImage.py
├── conda_requirements.txt
├── interwild
│   ├── fisheye_undist.py
│   ├── fisheye_webcam_cpp.py
│   ├── fisheye_webcam.py
│   ├── UndistortImage.py
│   └── webcam.py
├── pip_requirements.txt
├── README.md
└── webcam
    ├── png2video.py
    └── webcam.py
```

다음과 같이 Interwild Directory에 파일을 옮깁니다.
```
Interwild Directory
|-- data
|-- demo
|   ├── snapshot_6.pth
|   ├── fisheye_webcam.py
|   ├── fisheye_undist.py
|-- common
|-- main
|-- output
```