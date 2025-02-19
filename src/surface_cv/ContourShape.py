import cv2
import numpy as np

class ContourShape:
    def __init__(self):
        pass

    def find_two_most_similar_contours(self, image_contours, reference_contours):
        min_sims = []
        min_contours = []
        min_ref_contours = []
        for ref_contour in reference_contours:
            min_similarity, min_contour = self.most_similar_contour(image_contours, ref_contour)
            min_sims.append(min_similarity)
            min_contours.append(min_contour)
            min_ref_contours.append(ref_contour)
        min_sim = min(min_sims)
        min_contour = min_contours[min_sims.index(min_sim)]
        min_ref_contour = min_ref_contours[min_sims.index(min_sim)]
        return min_contour, min_ref_contour

    def most_similar_contour(self, contours, ref_contour):
        min_similarity = 1
        min_contour = None
        for contour in contours:
            similarity = cv2.matchShapes(ref_contour, contour, 1, 0.0)
            if similarity < min_similarity:
                min_similarity = similarity
                min_contour = contour
        return min_similarity, min_contour