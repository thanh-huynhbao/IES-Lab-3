import numpy as np
import cv2 as cv
import glob

path = '/home/isaacnewthanh/Documents/astra_23/'

chessBoardSize = (15,21)
frameSize =  (640,480)

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessBoardSize[0]*chessBoardSize[1],3), np.float32)
objp[:,:2] = np.mgrid[0:chessBoardSize[1],0:chessBoardSize[0]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob(path+'*.png')
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, chessBoardSize, None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, chessBoardSize, corners2, ret)
        cv.imshow('img', img)
        cv.waitKey()
if KeyboardInterrupt == 'q':
    cv.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print('camera matrix: ',mtx)
print('dist para: ',dist)
print('rotation matrix: ',rvecs)
print('translation matrix: ',tvecs)
