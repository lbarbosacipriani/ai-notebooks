import math

from cv2 import moments


def calc_angs(img_gsc):
    m = moments(img_gsc)
    cen_x = m['m10'] / m['m00']
    cen_y = m['m01'] / m['m00']
    theta = 0.5 * math.atan2(2 * m['mu11'], m['mu20'] - m['mu02'])
    return cen_x,cen_y,theta