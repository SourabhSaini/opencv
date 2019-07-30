import numpy as np
import cv2

# # Image Test
# img = cv2.imread('test_img.jpg', 0)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('test_gray.jpg', img)

# -----------------------------------------
# # Camera Video Test
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
#     cv2.imshow('gray', gray)
#     cv2.imshow('video', frame)
#     cv2.imshow('hsv', hsv)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# -----------------------------------------
# # Save Video
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('vid.avi', fourcc, 20, (640, 480))
# while cap.isOpened():
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     out.write(hsv)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# -----------------------------------------
# # Drawing Functions
# img = np.zeros((512, 512, 3), np.uint8)     # Create a black image
#
# cv2.line(img, (10, 10), (51, 300), (255, 0, 0), 5)  # Draw a inclined blue line with thickness of 5 px
#
# cv2.circle(img, (256, 256), 150, (0, 0, 255), 5)    # Draw a circle red line with thickness of 5 px
#
# cv2.rectangle(img, (40, 200), (200, 40), (0, 255, 0), 5)    # Draw a rectangle green line with thickness of 5 px
#
# cv2.ellipse(img, (300, 300), (100, 50), 30, 0, 360, (255, 255, 0), -1)    # Draw a ellipse cyan line
#
# vertices = np.array([[10, 10], [30, 90], [300, 120], [400, 10]], np.int32)
# vertices = vertices.reshape((-1, 1, 2))
# cv2.polylines(img, [vertices], True, (0, 255, 255), 5)
#
# cv2.putText(img, 'Text', (0, 500), cv2.FONT_HERSHEY_COMPLEX, 5, (150, 150, 150), 8)
#
# cv2.imshow('draw', img)
# cv2.waitKey(0)
# -----------------------------------------

# # Mouse as a Paint brush
# drawing = False     # true if mouse is pressed
# mode = True         # if True, draw rectangle. Press 'm' to toggle to curve
# ix, iy = -1, -1
#
#
# # mouse callback function
# def draw_circle(event, x, y, flags, param):
#     global ix, iy, drawing, mode
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing is True:
#             if mode is True:
#                 cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#             else:
#                 cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode is True:
#             cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#         else:
#             cv2.circle(img, (x, y), 50, (0, 0, 255), -1)
#
#
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
#
# while True:
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == ord('q'):
#         break
#
# cv2.destroyAllWindows()

# -----------------------------------------
# # Draw line with mouse
# img = np.zeros((512, 512, 3))
# draw = False
# ix, iy = 0, 0
#
#
# def draw_line(event, x, y, flags, param):
#     global ix, iy, draw
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print('DOWN', event)
#         draw = True
#         ix, iy = x, y
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if draw is True:
#             print('MOVE', event)
#             print(x, y, ix, iy)
#             cv2.line(img, (ix, iy), (x, y), (255, 255, 255), 3)
#             ix, iy = x, y
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         print('UP', event)
#         draw = False
#
#
# cv2.namedWindow('draw_line')
# cv2.setMouseCallback('draw_line', draw_line)
# while True:
#     cv2.imshow('draw_line', img)
#
#     if cv2.waitKey(20) == ord('q'):
#         break
# cv2.destroyAllWindows()
# -----------------------------------------

# Trackbar creation and get position
# img = np.zeros((512, 512, 3))
# cv2.namedWindow('trackbar')
#
#
# def nothing(x):
#     pass
#
#
# cv2.createTrackbar('Number', 'trackbar', 0, 1000, nothing)
# inum=0
# while True:
#     cv2.imshow('trackbar', img)
#
#     if cv2.waitKey(20) == ord('q'):
#         break
#
#     num = cv2.getTrackbarPos('Number', 'trackbar')
#     if inum != num:
#         img[:] = 0
#     inum = num
#     cv2.putText(img, str(num), (0, 256), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 255, 255), 8)
#
# cv2.destroyAllWindows()
# Access image and pixels
# img = cv2.imread('test_img.jpg')
# px = img[100, 100]           # Accessing pixel value
# print(px)
# blue = img[100, 100, 0]      # Accessing only blue pixel
# print(blue)
# img[100, 100] = [0, 0, 0]    # Modifying pixel value
# print(img[100, 100])
# Better/Optimized accessing image and pixels
# img = cv2.imread('test_img.jpg')
# px = img.item(10, 10, 1)        # Accessing pixel value
# print(px)
# img.itemset((10, 10, 1), 100)   # Modifying pixel value
# print(img.item(10, 10, 1))
# Accessing image properties
# img = cv2.imread('test_img.jpg')
# print(img.shape)
# print(img.size)
# print(img.dtype)
# -----------------------------------------

# Region of Interest ROI
# img = cv2.imread('test_img.jpg')
# part = img[500:700, 800:1000]
# cv2.namedWindow('part')
# while True:
#     cv2.imshow('part', part)
#     if cv2.waitKey(20) == ord('q'):
#         break
# cv2.destroyAllWindows()
# Split & Merge image channels
# img = cv2.imread('test_img.jpg')
# b, g, r = cv2.split(img)
# merged = cv2.merge((b, g, r))
# cv2.namedWindow('b')
# cv2.namedWindow('g')
# cv2.namedWindow('r')
# cv2.namedWindow('merge')
# while True:
#     cv2.imshow('b', b)
#     cv2.imshow('g', g)
#     cv2.imshow('r', r)
#     cv2.imshow('merge', merged)
#     if cv2.waitKey(20) == ord('q'):
#         break
# cv2.destroyAllWindows()
# -----------------------------------------

# Arithmetic operation on Images
# img = cv2.imread('test_img.jpg')
# img1 = cv2.imread('test_img1.jpg')
# add_opencv = cv2.add(img[0:534, 0:688], img1[0:534, 0:688])     # Always better than numpy coz it saturated operation
# add_numpy = img[0:534, 0:688] + img1[0:534, 0:688]              # Modulo operation
# cv2.namedWindow('opencv')
# cv2.namedWindow('numpy')
# while True:
#     cv2.imshow('opencv', add_opencv)
#     cv2.imshow('numpy', add_numpy)
#     if cv2.waitKey(20) == ord('q'):
#         break
# cv2.destroyAllWindows()
# -----------------------------------------

# Blending - Add weights
# img = cv2.imread('test_img.jpg')
# img1 = cv2.imread('test_img1.jpg')
# blend = cv2.addWeighted(img[0:534, 0:688], 1, img1[0:534, 0:688], 0.2, 0)
# cv2.namedWindow('blend')
# while True:
#     cv2.imshow('blend', blend)
#     if cv2.waitKey(20) == ord('q'):
#         break
# cv2.destroyAllWindows()
# -----------------------------------------

# Object Extraction in Image using OpenCV
# img = cv2.imread('test_img.jpg')
#
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# lower_red = np.array([-10, 100, 100])
# upper_red = np.array([10, 255, 255])
#
# lower_blue = np.array([110, 50, 50])
# upper_blue = np.array([130, 255, 255])
#
# mask1 = cv2.inRange(hsv, lower_red, upper_red)
# mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
#
# # Bitwise-AND mask and original image
# res = cv2.bitwise_and(img, img, mask=mask1)
# res = cv2.bitwise_and(img, img, dst=res, mask=mask2)
#
# cv2.namedWindow('res')
# while True:
#     cv2.imshow('res', res)
#     if cv2.waitKey(20) == ord('q'):
#         break
# cv2.destroyAllWindows()
# -----------------------------------------

# Object Extraction in Video using OpenCV
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([167, 102, -15])
    upper_red = np.array([187, 122,  65])

    # lower_blue = np.array([110, 50, 50])
    # upper_blue = np.array([130, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    # mask2 = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask1)
    # res = cv2.bitwise_and(frame, frame, dst=res, mask=mask2)

    cv2.namedWindow('res')

    cv2.imshow('res', res)
    if cv2.waitKey(20) == ord('q'):
        break
cv2.destroyAllWindows()

#
# image_hsv = None
# pixel = (0, 0, 0)
#
#
# # mouse callback function
# def pick_color(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         pixel = image_hsv[y, x]
#
#         # you might want to adjust the ranges(+-10, etc):
#         upper = np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
#         lower = np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
#         print(pixel, lower, upper)
#
#         image_mask = cv2.inRange(image_hsv, lower, upper)
#         cv2.imshow("mask", image_mask)
#
#
# def main():
#     global image_hsv, pixel
#
#     image_src = cv2.imread('logo.jpg')  # pick.py my.png
#     cv2.imshow("bgr", image_src)
#
#     cv2.setMouseCallback('bgr', pick_color)
#
#     image_hsv = cv2.cvtColor(image_src, cv2.COLOR_BGR2HSV)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# if __name__=='__main__':
#     main()