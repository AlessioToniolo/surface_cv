import ImageProcessing
import cv2
import os

class ReferenceContours:
    def __init__(self, processor: ImageProcessing):
        self.processor = processor
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "reference.jpg")

    def get_reference_contours(self):
        img = cv2.imread(image_path)
        contours = self.processor.get_contours(img)
        return contours

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "reference.jpg")
    img = cv2.imread(image_path)
    contours = ImageProcessing.ImageProcessing().get_contours(img)
    print(f"Number of contours found: {len(contours)}")
    img_with_contours = img.copy()
    cv2.drawContours(img_with_contours, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Contours', img_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()