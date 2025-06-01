import os
import cv2

# read image
image_name = 'duck.jpg'
image_path = os.path.join('.', 'data', image_name)
image = cv2.imread(image_path)
print(image.shape)

# write image
cv2.imwrite(os.path.join('.', 'data', 'duck_out.jpg'), image)

# visualize image
cv2.imshow(image_name, image)
cv2.waitKey(0)