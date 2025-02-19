import Camera
import ImageProcessing
import cv2
import os
import time

if __name__ == "__main__":
    cam = Camera.Camera()

    """
    img = cam.get_image()
    img_contours = ImageProcessing.ImageProcessing().get_contours(img)

    # find largest contour by area
    largest_contour = None
    max_area = 0
    for contour in img_contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour = contour

    img_with_contours = img.copy()


    #cv2.drawContours(img_with_contours, img_contours, -1, (0, 255, 0), 2)
    # draw largest contour
    cv2.drawContours(img_with_contours, [largest_contour], -1, (0, 255, 0), 2)


    cv2.imshow('Contours', img_with_contours)
    cv2.waitKey(5)
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "reference.jpg")
    img = cv2.imread(image_path)
    img_contours = ImageProcessing.ImageProcessing().get_contours(img)

    largest_contour = None
    max_area = 0
    for contour in img_contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour = contour

    img_with_contours = img.copy()
    cv2.drawContours(img_with_contours, [largest_contour], -1, (0, 255, 0), 2)
    cv2.imshow('Contours', img_with_contours)
    cv2.waitKey(5)




    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "reference.jpg")
    ref = cv2.imread(image_path)
    ref_contours = ImageProcessing.ImageProcessing().get_contours(ref)
    ref_with_contours = ref.copy()
    cv2.drawContours(ref_with_contours, ref_contours, -1, (0, 255, 0), 2)
    cv2.imshow('Reference Contours', ref_with_contours)
    cv2.waitKey(5)
    time.sleep(10)
    cam.stop()
