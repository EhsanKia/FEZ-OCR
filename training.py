import cv2
import numpy as np
import detector

# load up our training image and parse it for glyphs
alphabet_im = cv2.imread('img/alphabet.png')
boxes, thresh = detector.find_boxes(alphabet_im, 48)

samples = np.empty((0, 100))
responses = []
for x1, y1, x2, y2 in reversed(boxes):
    # Shows that one glyph to the user
    cv2.imshow('Train', alphabet_im[y1:y2, x1:x2])

    # gets user's response
    responses.append(cv2.waitKey())

    # Cuts the sample, resizes and stores it
    sample = cv2.resize(thresh[y1:y2, x1:x2], (10, 10)).reshape((1, 100))
    samples = np.append(samples, sample, 0)

# Saves all the data to file
np.savetxt('responses.data', np.array(responses))
np.savetxt('training.data', samples)

# Close the display window
cv2.destroyWindow("Train")