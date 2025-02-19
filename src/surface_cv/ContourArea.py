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
    
    def filter_contours(self, contours, ref_area, threshold_percent=0.3):
        filtered_contours = []
        for contour in contours:
            contour_area = cv2.contourArea(contour)
            # filter if bigger or smaller than threshold
            if contour_area > ref_area * (1 + threshold_percent) or contour_area < ref_area * (1 - threshold_percent):
                filtered_contours.append(contour)
        return filtered_contours