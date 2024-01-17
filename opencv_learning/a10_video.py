import cv2

def main():
    cap = cv2.VideoCapture(0)
    con = True
    while con:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            con = False

if __name__ == "__main__":
    main()