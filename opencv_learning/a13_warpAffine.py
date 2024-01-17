import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    con = True
    M1 = cv2.getRotationMatrix2D((0, 0), 45, 1)
    M1[0][2] += 200
    M1[1][2] += 200
    M2 = cv2.getAffineTransform(
        np.float32([[0, 0], [0, 100], [100, 0]]),
        np.float32([[30, 0], [30, 200], [130, 0]])
    )
    while con:
        ret, frame = cap.read()
        if ret:
            frame = cv2.warpAffine(frame, M2, (frame.shape[1], frame.shape[0]))
            cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            con = False

if __name__ == "__main__":
    main()