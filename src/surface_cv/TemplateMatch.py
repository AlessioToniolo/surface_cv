import ContourArea

class TemplateMatch: 
    def __init__():
        pass

    def match(self, img_contours, ref_contours):
        ca = ContourArea()
        ref_contour, ref_area = ca.find_biggest_contour(ref_contours)
        filtered_contours = ca.filter_contours(img_contours, ref_area)