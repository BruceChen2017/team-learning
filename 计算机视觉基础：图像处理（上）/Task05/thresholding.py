import cv2 as cv

p1 = r"rabbit.jpg"
img1 = cv.imread(p1)

# simple thresholding(global)
src1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
threshold, dst11 = cv.threshold(src1, 100, 255, cv.THRESH_BINARY) # predefined thresh
print("Predefined threshold:", threshold)
# OSTU
ostu_thresold, dst12 = cv.threshold(src1, 100, 255, cv.THRESH_OTSU) # thresh has no effect here
print("Calculated OSTU threshold:", ostu_thresold)
cv.imshow("Original gray image: rabbit", src1)
cv.imshow("Binary threshold", dst11)
cv.imshow("OSTU threshold", dst12)
cv.waitKey(0)
cv.destroyAllWindows()

p2 = r"sudoku.png"
# adaptive thresholding(local)
img2 = cv.imread(p2)
src2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
_, dst20 = cv.threshold(src2, 100, 255, cv.THRESH_BINARY)
dst21 = cv.adaptiveThreshold(src2, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 3)
dst22 = cv.adaptiveThreshold(src2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 3)
cv.imshow("Original gray image: sudoku", src2)
cv.imshow("Simple binary threshold", dst20)
cv.imshow("ADAPTIVE THRESH MEAN", dst21)
cv.imshow("ADAPTIVE THRESH GAUSSIA", dst22)
cv.waitKey(0)

