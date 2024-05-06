import cv2
import argparse
import os.path as osp
import numpy as np
import os

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', default='./webcam/', type=str)

    args = parser.parse_args()

    return args

def visualize(original_img,pred):
    res_img = original_img.copy()
    #res_img = np.concatenate((res_img,pred), axis=1)
    return res_img

def ImShow(input_img):
    #input_img = cv2.cvtColor(input_img,cv2.COLOR_RGB2BGR)

    cv2.imshow('image',input_img)
    cv2.waitKey(1)

def main():

    args = arg_parse()
    webcam = cv2.VideoCapture(0) 
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    # frame을 가져오는 부분
    cur_frame = 0
    print(args.img_path)
    while(True):

        retval, img_original_bgr = webcam.read()
        h,w = img_original_bgr.shape[:2]

        
        ## left
        img_original_bgr = img_original_bgr[:,:w//2,:]
        '''
        ## right
        img_original_bgr = img_original_bgr[:,w//2:,:]
        '''
        img_path = osp.join(args.img_path,f'{cur_frame:05d}.jpg')
        if retval:
            
            if cv2.waitKey(1) & 0xFF == ord('s'):
                while os.path.exists(img_path):
                    cur_frame += 1
                    img_path = osp.join(args.img_path,f'{cur_frame:05d}.jpg')
                cv2.imwrite(img_path,img_original_bgr)
                print(f'save{cur_frame}')
                cur_frame += 1
        else:
            print('No Frames')
            break
        

        # frame을 이용해서 model 처리
        '''
        output = model(img_original_bgr.copy())
        draw_pred_output = draw_2d_joint()
        '''
    
        # 최종적으로 np.array형태의 img array가 있으면 됌
        res_img = visualize(img_original_bgr,img_original_bgr) # 두번째 인자를 model output으로 변경
        ImShow(res_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    webcam.release()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
    