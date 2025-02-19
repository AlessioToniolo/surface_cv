import cv2
import numpy as np

class ContourShape:
    def __init__(self):
        pass

    def filter_contours(self, contours, ref_contour, threshold=0.1):
        min_similarity = 1
        for contour in contours:
            similarity = cv2.matchShapes(ref_contour, contour, 1, 0.0)
            print(similarity)
            if similarity < threshold:
                filtered_contours.append(contour)
        return filtered_contours