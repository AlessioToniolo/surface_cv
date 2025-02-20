#import Camera
import ImageProcessing
import cv2
import os
import time
import ContourShape

if __name__ == "__main__":
    #cam = Camera.Camera()

    
    #img = cam.get_image()
    #img_contours = ImageProcessing.ImageProcessing().get_contours(img)
    #img_with_contours = img.copy()

    #cv2.drawContours(img_with_contours, img_contours, -1, (0, 255, 0), 2)

    #cv2.imshow('Contours', img_with_contours)
    #cv2.waitKey(5)
    
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
    """



    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "reference.jpg")
    ref = cv2.imread(image_path)
    ref_contours = ImageProcessing.ImageProcessing().get_contours(ref)
    print(len(ref_contours))
    ref_with_contours = ref.copy()
    cv2.drawContours(ref_with_contours, ref_contours, -1, (0, 255, 0), 2)
    cv2.imshow('Reference Contours', ref_with_contours)
    cv2.waitKey(5)


    image_path2 = os.path.join(current_dir, "IMG_7538.png")

    img = cv2.imread(image_path2)
    img_contours = ImageProcessing.ImageProcessing().get_contours(img)
    print(len(img_contours))
    img_with_contours = img.copy()

    cs = ContourShape.ContourShape()
    min_contour, min_ref_contour = cs.find_two_most_similar_contours(img_contours, ref_contours)
    print(min_contour)
    print(min_ref_contour)
    #cv2.drawContours(img_with_contours, [min_contour], -1, (0, 255, 0), 2)

    cv2.drawContours(img_with_contours, img_contours, -1, (0, 255, 0), 2)
    cv2.imshow('Img Contours', img_with_contours)
    cv2.waitKey(5)
    time.sleep(5)
    #cam.stop()
