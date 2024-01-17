import cv2

def main():
    # /home/dy/First-step/opencv_learning/data/lena.jpg

    
    img = cv2.imread("/home/dy/First-step/opencv_learning/data/lena.jpg", 1)
    cv2.imwrite("/home/dy/First-step/opencv_learning/output/lena_copy.png", img)
    
    cv2.imwrite("/home/dy/First-step/opencv_learning/output/lena_copy.bmp", img)
    
    cv2.imwrite("/home/dy/First-step/opencv_learning/output/lena_copy_50.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 50])

    cv2.imwrite("/home/dy/First-step/opencv_learning/output/lena_copy_8.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 8])




if __name__ == "__main__":
    main()