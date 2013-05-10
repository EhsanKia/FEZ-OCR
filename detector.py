import cv2

# Checks if two half rectangles are close
def find_near(splits, x, y, size):
    for i, s in enumerate(splits):
        x2 = s[0] + s[2] / 2
        y2 = s[1] + s[3] / 2
        dist_squared = (x - x2) ** 2 + (y - y2) ** 2
        if dist_squared < (size * 0.7) ** 2:
            return i
    return -1

# Connects two half rectangles
def join_rect(rect1, rect2):
    x1 = min(rect1[0], rect2[0])
    y1 = min(rect1[1], rect2[1])
    x2 = max(rect1[0] + rect1[2], rect2[0] + rect2[2])
    y2 = max(rect1[1] + rect1[3], rect2[1] + rect2[3])
    return x1, y1, x2, y2

# Finds all the glyphs
def find_boxes(im, size):
    # Does some preprocessing
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)    
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 0, 127, 0)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    thresh2 = cv2.adaptiveThreshold(gray, 255, 1, 1, 127, 0)
    contours2, _ = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Checks if image needs to be inverted
    if len(contours2) > len(contours):
        thresh = thresh2
        contours = contours2

    boxes = []
    splits = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > size * 2 or h > size * 2:  # Too big
            continue

        if w >= size and h >= size: # Perfect size
            boxes.append((x, y, x + w, y + h))

        elif w >= size or h >= size: # half box
            # Tries to find other half
            i = find_near(splits, x + w / 2, y + h / 2, size)
            if i > -1: # If it finds it, connects them
                other = splits.pop(i)
                x1, y1, x2, y2 = join_rect((x, y, w, h), other)
                boxes.append((x1, y1, x2, y2))
            else: # Else, stores for later
                splits.append((x, y, w, h))
                
    # returns all the boxes and the processed image
    return boxes, thresh