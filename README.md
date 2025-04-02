# Lets-Calibrate-and-Correct
It is a program that recognizes the chessboard of the video, performs calibration, and corrects lens distortion!

When you put a video of the chessboard into the program, the grid points of the chessboard are identified and calibrated. Even if the video is taken from various points of view, it performs well, and when the calibration is over, the lens distortion is corrected using the results.

Camera Matrix (K):
 [[8.79221371e+03 0.00000000e+00 4.48651014e+02]
 [0.00000000e+00 5.58395094e+03 2.03414414e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
Distortion Coefficients:
 [[ 1.31373688e+01 -2.35946776e+03  5.29334440e-01  1.71694993e-01   9.89431924e+03]]
RMSE: 0.8601977910393672

Undistorted Demo(also in this repository) : https://drive.google.com/file/d/1ZGYdfq_q7L5tHnWyg1IjZrLsCEolite5/view?usp=drive_link
Example video : https://drive.google.com/file/d/1G21xZ6bHscidv8C74ZmIi88HSUlrn_Rr/view?usp=drive_link
