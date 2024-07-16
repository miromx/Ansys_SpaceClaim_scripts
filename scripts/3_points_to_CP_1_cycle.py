"""
Read sorted coordinate file
Find Chebyshev's nodes
Write down Chebyshev's nodes
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import math
import re
from scipy.interpolate import interp1d

templ_s = r'\d+\.\d*'
path = r'~'  # work folder
try:
    os.mkdir(os.path.join(r'~', 'scdm_cp_xy_coord'), mode=0o777, dir_fd=None)
    print('ok')
except FileExistsError:
    print('already exists')
path_target = '~'


def cheb_points1(n, a, b):
    """
    Generating Chebyshev's nodes
    :param n:
    :param a:
    :param b:
    :return:
    """
    return [((a - b) * math.cos((2. * i + 1.) / (2. * n) * math.acos(-1.)) + a + b) / 2. for i in range(n)]


def cheb_points2(n, a, b):
    """
    Generating Chebyshev's nodes
    :param n:
    :param a:
    :param b:
    :return:
    """
    return [0.5 * (a + b) + 0.5 * (b - a) * math.cos(((2. * i - 1) / (2 * n)) * math.pi) for i in range(n)]


for filename in os.listdir(path):
    print(filename)
    # filename = '1_result_z=0.15.txt_for_Chebishev_Points.txt'  # file
    f = np.genfromtxt(os.path.join(path, filename), skip_header=False)
    print(f.shape[0])
    mn = int(math.ceil(f.shape[0]/2))
    # print('mn=', mn)
    # lower half original
    x_n = f[:mn, 0]
    y_n = f[:mn, 1]
    # print('x_n= {}'.format(x_n))

    # upper half original
    x_v = f[-mn:, 0]
    y_v = f[-mn:, 1]
    # print('x_v= {}'.format(x_v))

    a = x_n[-1]     # range from a (beginning of the segment)
    print(a)
    b = x_n[0]      # range up to b (end of segment)
    print(b)

    f = interp1d(x_n, y_n, kind='cubic')    # interpolate the original lower points
    f2 = interp1d(x_v, y_v, kind='cubic')   # interpolate the original top points

    x_cp = cheb_points2(7, b, a)            # x-coordinates of Chebyshev's nodes on a segment (number of nodes by default = 7)

    y_cp_bottom = f(x_cp)
    y_cp_upper = f2(x_cp)
    hc = []     # deviation from x-axis (midline)
    h = []      # half-height of each section at the Chebyshev's node
    print('{:*^30}'.format('begin'))
    for i, j in zip(y_cp_upper, y_cp_bottom):
        h_t = (i - j) / 2           # half-height of each section at the Chebyshev node
        yc_t = (j + (i - j) / 2)    # deviation from x-axis (midline)
        hc.append(yc_t)
        h.append(h_t)
    x0 = x_v[0];
    print('x0 = {}'.format(x0))
    y0 = y_v[0];
    print('y0 = {}'.format(y0))
    nos = np.array([x0, y0])
    # hc.insert(0, y_v[0])  # deviation from x-axis (midline) nose point
    hc.append(y_v[-1] - (y_v[-1] - y_n[0]) / 2)  # deviation from x-axis (midline) extreme point
    print('hc = {}'.format(hc))

    # h.insert(0, y_v[0])  # deviation from x-axis (midline) nose point
    h.append((y_v[-1] - y_n[0]) / 2)  # deviation from x-axis (midline) extreme point
    print('h= {}'.format(h))

    xc = x_cp.copy()
    # xc.insert(0, x_v[0]) # head point
    xc.append(x_v[-1])
    print('xc = {}'.format(xc))
    print(len(xc), len(hc), len(h))
    print('{:*^30}'.format('end'))

    plt.plot(x_n, y_n, 'y--', label=' bottom origin(y_n) ')
    plt.plot(x_v, y_v, 'm--', label=' top origin(y_v) ')
    plt.plot(x_cp, y_cp_bottom, 'b-', marker='.', label='BOTTOM(y_cp_bottom)')
    plt.plot(x_cp, y_cp_upper, 'r-', marker='.', label='UPPER(y_cp_upper)')
    # plt.plot(xc, h, 'c.', marker='d', label=' h')
    plt.plot(xc, hc, 'g', marker='d', label=' hc ')
    plt.grid()
    plt.minorticks_on()
    plt.legend()
    plt.show()
    print('DONE')

    mask = re.findall(templ_s, filename)
    print(*mask)

    
    np.savetxt(path_target + 'xc={}.txt'.format(*mask), xc, fmt='%.4f')
    np.savetxt(path_target + 'hc={}.txt'.format(*mask), hc, fmt='%.4f')
    np.savetxt(path_target + 'h={}.txt'.format(*mask), h, fmt='%.4f')
    np.savetxt(path_target + 'nos={}.txt'.format(*mask), nos, fmt='%.4f')
