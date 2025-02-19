class TemplateMatch: 
    def __init__():
        pass

    def match(self, image_contours, template_contours):
    
        # find largest contour by area
        largest_contour = None
        max_area = 0
        for contour in image_contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                largest_contour = contour

        # find largest contour by area
        largest_template_contour = None
        max_area = 0
        for contour in template_contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                largest_template_contour = contour

        # find the best match
        result = cv2.matchShapes(largest_contour, largest_template_contour, 1, 0.0)
        return result