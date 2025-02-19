from dataclasses import dataclass
import numpy as np
import pyrealsense2 as rs
import cv2

class Camera:
    def __init__(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
    
    def get_image(self):
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.pipeline.start(self.config)

        for i in range(30):
            frames = self.pipeline.wait_for_frames()

        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())

        return color_image
    
    def stop(self):
        self.pipeline.stop()

if __name__ == "__main__":
    cam = Camera()
    color_image = cam.get_image()
    print(color_image.shape) # (480, 640, 3)
    cv2.imshow('Color Image', color_image)
    cv2.waitKey(1)
    cam.stop()
    cv2.destroyAllWindows()