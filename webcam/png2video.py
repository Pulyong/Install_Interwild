from tqdm import tqdm
import os
import cv2
import re
from glob import glob

def save_video(path, out_name):    
    file_path = sorted(glob(path+'/*.jpg'), key=lambda x: int(re.search(r'\d+', x.split('/')[-1]).group()))    
    #file_path = sorted(glob(path+'/*.png'), key=lambda x: int(re.search(r'\d+', x.split('/')[-1]).group()))    
    #print(file_path)
    #file_path = sorted(glob(path+'/*skeleton*.jpg'), key=lambda x: int(re.search(r'\d+', x.split('/')[-1]).group()))    
    #sorted(glob(path+'/*skeleton*.jpg'), key= lambda x: print(re.search(r'\d+',x.split('/')[-1]).group()))
    
    
    print('saving to :', out_name + '.mp4')
    img_array = []
    height, width = 0, 0
    for filename in tqdm(file_path):
        img = cv2.imread(filename)
        if height != 0:
            img = cv2.resize(img, (width, height))
        height, width, _ = img.shape
        size = (width,height)
        img_array.append(img)

    out = cv2.VideoWriter(out_name + '.mp4', 0x7634706d, 10, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print('done')
    

if __name__ == '__main__':
    save_video('/home/shu/Desktop/Yongjin/hands/git_models/InterWild/demo/fisheye/fisheye_webcam_cpp','/home/shu/Desktop/Yongjin/hands/git_models/InterWild/demo/fisheye/fisheye_webcam_cpp/webcam_cpp')