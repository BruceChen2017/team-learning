import cv2

if __name__ == "__main__":
    img = cv2.imread("rabbit.jpg", cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape) # (height, width)

    # 0.5*size
    fx = fy = 0.5
    re1 = cv2.resize(img, dsize=None, fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
    re2 = cv2.resize(img, dsize=None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)

    # 1.5*size
    factor = 1.5 
    # (width, height)
    dsize = (int(img.shape[1] * factor), int(img.shape[0] * factor))
    re3 = cv2.resize(img, dsize=dsize, interpolation=cv2.INTER_NEAREST)
    re4 = cv2.resize(img, dsize=dsize, interpolation=cv2.INTER_LINEAR)

    # show image
    cv2.imshow("Original imgage", img)
    cv2.imshow("0.5*size image by NEAREST", re1)
    cv2.imshow("0.5*size image by LINEAR", re2)
    cv2.imshow("1.5*size image by NEAREST", re3)
    cv2.imshow("1.5*size image by LINEAR", re4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
