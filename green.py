# import the necessary packages
import numpy as np
import argparse
import cv2
from time import sleep


([0, 150, 0], [0, 255, 255])




# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", help = "path to the image")
# args = vars(ap.parse_args())
# load the image
video = cv2.VideoCapture(0)
# image = cv2.imread("papa.png")


while True:
    ret, image = video.read()
    imagem = image
    if not ret:
          break
    

# define the list of boundaries
    boundaries = [
        ([150, 0, 0], [255, 255, 150]),     #azul
        ([0, 50, 150], [100, 255, 255]),    #amarelo
        ([36, 0, 0], [86, 230,230]),        #verde
        ([0, 0, 140], [110, 110,255])       #vermelho
    ]

    

    # for (lower1, upper1) in boundaries:
         
    #     lower1 = np.array(lower1, dtype = "uint8")
    #     upper1 = np.array(upper1, dtype = "uint8")
    #     mask = cv2.inRange(image, lower1, upper1)
    #     output = cv2.bitwise_and(image, image, mask = mask)
    #     cv2.imshow("image", np.hstack([image, output]))

    (lower1, upper1) = boundaries[0]
    lower1 = np.array(lower1, dtype = "uint8")
    upper1 = np.array(upper1, dtype = "uint8")
    mask = cv2.inRange(image, lower1, upper1)
    output = cv2.bitwise_and(image, image, mask = mask)
    cv2.imshow("azul", np.hstack([image, output]))


    (lower2, upper2) = boundaries[1]
    lower2 = np.array(lower2, dtype = "uint8")
    upper2 = np.array(upper2, dtype = "uint8")
    mask = cv2.inRange(imagem, lower2, upper2)
    output = cv2.bitwise_and(imagem, imagem, mask = mask)
    cv2.imshow("amarelo", np.hstack([imagem, output]))

    (lower3, upper3) = boundaries[2]
    lower3 = np.array(lower3, dtype = "uint8")
    upper3 = np.array(upper3, dtype = "uint8")
    mask = cv2.inRange(imagem, lower3, upper3)
    output = cv2.bitwise_and(imagem, imagem, mask = mask)
    cv2.imshow("verde", np.hstack([imagem, output]))
    
    (lower4, upper4) = boundaries[3]
    lower4 = np.array(lower4, dtype = "uint8")
    upper4 = np.array(upper4, dtype = "uint8")
    mask = cv2.inRange(imagem, lower4, upper4)
    output = cv2.bitwise_and(imagem, imagem, mask = mask)
    cv2.imshow("vermelho", np.hstack([imagem, output]))

    if cv2.waitKey(1) & 0xFF == ord('q'): break


video.release()
cv2.destroyAllWindows()