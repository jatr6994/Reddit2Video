import imageio
import os

filenames = [ "frames" + "/" + img for img in os.listdir( "frames" ) if img.endswith( ".png" ) ]

with imageio.get_writer('movie.mp4', mode='I', fps=60) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)



"""
# thanks https://stackoverflow.com/a/44948030

import cv2
import os

image_folder = 'frames'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
"""