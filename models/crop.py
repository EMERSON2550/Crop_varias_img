from glob import glob
import cv2

class CropImg:

    def salve_crop(self, bundbox, rotation):
        for path in glob("img_para_crop/*.jpg"):
            img = cv2.imread(path)
        
            #crop = img[200:1050, 100:2430] #crop Frisa saquencia y_min:y_max, x_min:x_max  
            crop = img[bundbox['y_min']:bundbox['y_max'], bundbox['x_min']:bundbox['x_max']]
            if rotation == 270:
                crop = cv2.rotate(crop, cv2.ROTATE_90_COUNTERCLOCKWISE)
            else:
                print('imagen com rotaçao errada')
            nome_img_nova = 'img_processo' + path[13:]
            cv2.imwrite(nome_img_nova, crop)