import numpy as np
from PIL import Image

def detect_image(yolo, input_img_path, output_img_path, exec_loop=False):
    continue_loop = True
    while continue_loop:
        try:
            image = Image.open(input_img_path)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
            import cv2
            img = np.array(r_image, dtype='float32')
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            cv2.imwrite(output_img_path,img)

        if exec_loop:
            input_str = input("Continue? (yes/[no])")
            if input_str.lower() != 'yes':
                continue_loop = False
        else:
            continue_loop = False

    yolo.close_session()