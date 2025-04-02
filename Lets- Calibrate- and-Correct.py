import cv2 as cv
import numpy as np
import threading

video_path = 'C:/Users/Hi/Desktop/chessboard.mp4'
board_size = (8, 6)

cap = cv.VideoCapture(video_path)

obj_points = [] 
img_points = [] 
objp = np.zeros((board_size[0] * board_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:board_size[0], 0:board_size[1]].T.reshape(-1, 2)

calibration_done = False
K = None
dist_coeff = None

def calibrate():
    global calibration_done, K, dist_coeff
    print("Starting calibration in background thread...")
    ret, K, dist_coeff, rvecs, tvecs = cv.calibrateCamera(obj_points, img_points, (640, 480), None, None)
    calibration_done = True
    print("Calibration completed!")
    print("Camera Matrix (K):\n", K)
    print("Distortion Coefficients:\n", dist_coeff)
    print("RMSE:", ret)

if not cap.isOpened():
    print("Error: Could not open video.")
else:
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        ret, corners = cv.findChessboardCorners(gray, board_size, cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE)

        if ret:
            cv.drawChessboardCorners(frame, board_size, corners, bool(ret))
            if len(obj_points) < 50:
                img_points.append(corners)
                obj_points.append(objp)
                if len(obj_points) % 10 == 0 and not calibration_done:
                    threading.Thread(target=calibrate).start()
        else:
            cv.putText(frame, "No Chessboard", (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv.imshow("Calibration", frame)
        frame_count += 1

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cap = cv.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)

        h, w = frame.shape[:2]
        new_camera_matrix, roi = cv.getOptimalNewCameraMatrix(K, dist_coeff, (w, h), 1, (w, h))
        undistorted_frame = cv.undistort(frame, K, dist_coeff, None, new_camera_matrix)

        cv.putText(undistorted_frame, "Undistorted", (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.imshow("Distortion Correction", undistorted_frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
    print("Process ended.")