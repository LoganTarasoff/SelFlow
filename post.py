import cv2
import tensorflow as tf
import numpy as np
from flowlib import read_flo
from scipy import misc, io


def computeMeanVector(flo):
    u = flo[:,:,0]
    v = flo[:,:,1]
    u_mean = np.mean(u)
    v_mean = np.mean(v)
    angle = np.arctan2(u_mean, v_mean)
    mag = np.sqrt((u_mean**2 + v_mean**2))
    return u_mean, v_mean, angle, mag


#def annotateVector(img,u_mean, v_mean, angle, mag):
#    color = (255, 0, 0)
#    thickness = 2
#    pt1 = (360, 270)
#    pt2 = (u_mean.astype(int) + 360, v_mean.astype(int) + 270)
#    deg = "{0:.3f} deg"
#    pixels = "{0:.3f} pixels"
#    sum = "{0:.3f} pixels total"
#    img = cv2.arrowedLine(img, pt1, pt2, color, thickness, 8, 0, 0.5)
#    img = cv2.putText(img, deg.format(angle), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
#    img = cv2.putText(img, pixels.format(mag), (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
#    img = cv2.putText(img, sum.format(distance), (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)


#def displayImageFromPath(path, i):
#    img = cv2.imread(path, 1)
#    annotateVector(img, u_mean, v_mean, angle, mag)
#    cv2.imshow('image', img)
#    misc.imsave('%s/annotated_%s.png' % ('images/test_images', i), img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

distance = 0
imgpath = 'images/test_images/frame_000{}.png'
flopath = 'images/test_images/flow_fw_000{}.flo'
for i in range(5, 10):
    flo = read_flo(flopath.format(i))
    u_mean, v_mean, angle, mag = computeMeanVector(flo)
    distance += mag
#    displayImageFromPath(imgpath.format(i), i)
imgpath = 'images/test_images/frame_000{}.png'
flopath = 'images/test_images/flow_fw_000{}.flo'
for i in range(5, 8):
    flo = read_flo(flopath.format(i))
    u_mean, v_mean, angle, mag = computeMeanVector(flo)
    distance += mag
#    displayImageFromPath(imgpath.format(i), i)
