import cv2
import os
from Camera import Camera

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    cam = Camera()
    image = cam.get_image()
    
    filename = "reference.jpg"
    filepath = os.path.join(current_dir, filename)
    cv2.imwrite(filepath, image)
    
    print(f"Image saved to {filepath}")
    cam.stop()  