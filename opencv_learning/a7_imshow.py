import cv2

def main():
    # /home/dy/First-step/opencv_learning/data/lena.jpg

    
    img = cv2.imread("/home/dy/First-step/opencv_learning/data/lena.jpg", 1)
    cv2.imshow("lena", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()