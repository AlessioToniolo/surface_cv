import cv2
import numpy as np
import os

def improved_watershed(image):
    # Convert to grayscale if not already
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
    
    # Better binary image creation
    # Use Otsu's thresholding with a bias toward capturing the dark part
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Fill small holes in the part
    kernel = np.ones((5, 5), np.uint8)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    # Remove small noise blobs
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
    
    # Watershed process with refinements
    # Create sure background - dilate less to avoid oversegmentation
    sure_bg = cv2.dilate(binary, kernel, iterations=1)
    
    # Create sure foreground with more conservative threshold
    dist = cv2.distanceTransform(binary, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist, 0.6 * dist.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    
    # Unknown region
    unknown = cv2.subtract(sure_bg, sure_fg)
    
    # Marker labeling
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    
    # Apply watershed
    color_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) if len(image.shape) == 2 else image.copy()
    markers = cv2.watershed(color_image, markers)
    
    # Post-process the markers to clean up the result
    # Create a clean mask just for the part
    part_mask = np.zeros_like(gray)
    for i in range(2, np.max(markers) + 1):
        # Get the size of each segment
        segment_size = np.sum(markers == i)
        # Keep only larger segments - adjust threshold as needed
        if segment_size > 1000:  # Minimum area threshold
            part_mask[markers == i] = 255
    
    # Find contours of the mask to get the final part outline
    contours, _ = cv2.findContours(part_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # If contours were found, keep only the largest one
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        final_mask = np.zeros_like(gray)
        cv2.drawContours(final_mask, [largest_contour], 0, 255, -1)
        
        # Recreate markers with just the largest component
        clean_markers = np.ones_like(markers)
        clean_markers[final_mask == 255] = 2
        clean_markers[markers == -1] = -1  # Keep watershed lines
        
        return clean_markers, binary
    
    return markers, binary

# Example usage
if __name__ == "__main__":
    # Load image
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "cont.png")
    image = cv2.imread(image_path)
    
    # Apply improved watershed
    markers, binary = improved_watershed(image)
    
    # Create result visualization
    result = image.copy()
    
    # Draw watershed boundaries in green
    result[markers == -1] = [0, 255, 0]
    
    # Create mask for the part (any marker value > 1)
    part_mask = np.zeros_like(markers, dtype=np.uint8)
    part_mask[markers > 1] = 255
    
    # Find contour of the part
    contours, _ = cv2.findContours(part_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Get largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Draw contour
        cv2.drawContours(result, [largest_contour], -1, (0, 255, 0), 2)
        
        # Calculate centroid and orientation
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(result, (cx, cy), 5, (0, 0, 255), -1)
            
            # Calculate orientation
            rect = cv2.minAreaRect(largest_contour)
            box = cv2.boxPoints(rect)
            box = np.int32(box)  # Changed from np.int0 to np.int32np.int32
            
            # Ensure box points are valid before drawing
            if box.shape[0] > 0:
                cv2.drawContours(result, [box], 0, (255, 0, 0), 2)
            
            # Angle calculation with better handling
            angle = rect[2]
            if angle < -45:
                angle += 90
            print(f"Part centroid: ({cx}, {cy})")
            print(f"Part orientation: {angle:.2f} degrees")
    
    # Display results
    cv2.imshow('Binary', binary)
    cv2.imshow('Watershed Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
