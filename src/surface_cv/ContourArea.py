import cv2
import numpy as np

class ContourArea:
    def __init__(self):
        pass

    def find_biggest_contour(self, contours):
        largest_contour = None
        max_area = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                largest_contour = contour

        return largest_contour, max_area