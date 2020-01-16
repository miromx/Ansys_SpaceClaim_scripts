"""
25.11.2019
считать отсортированный координатный файл
найти т Чебышева
записать т Чебышева
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import math
import re
from scipy.interpolate import interp1d

shablon = r'\d+\.\d*'
path = r'~'  # целевая папка
try:
    os.mkdir(os.path.join(r'~', 'scdm_cp_xy_coord'), mode=0o777, dir_fd=None)
    print('ok')
except FileExistsError:
    print('уже есть')
path_target = '~'


def cheb_points1(n, a, b):
    """
    Generating Chebyshev knots
    :param n:
    :param a:
    :param b:
    :return:
    """
    return [((a - b) * math.cos((2. * i + 1.) / (2. * n) * math.acos(-1.)) + a + b) / 2. for i in range(n)]


def cheb_points2(n, a, b):
    """
    Generating Chebyshev knots
    :param n:
    :param a:
    :param b:
    :return:
    """
    return [0.5 * (a + b) + 0.5 * (b - a) * math.cos(((2. * i - 1) / (2 * n)) * math.pi) for i in range(n)]


for filename in os.listdir(path):
    print(filename)
    # filename = '1_result_z=0.15.txt_for_Chebishev_Points.txt'  # целевой файл
    f = np.genfromtxt(os.path.join(path, filename), skip_header=False)
    print(f.shape[0])
    mn = int(math.ceil(f.shape[0]/2))
    # print('mn=', mn)
    # нижняя половина исходные
    x_n = f[:mn, 0]
    y_n = f[:mn, 1]
    # print('x_n= {}'.format(x_n))

    # верхняя половина исходные
    x_v = f[-mn:, 0]
    y_v = f[-mn:, 1]
    # print('x_v= {}'.format(x_v))

    a = x_n[-1]  # диапазон от а (начало отрезка)
    print(a)
    b = x_n[0]  # диапазон до b (конец отрезка)
    print(b)

    f = interp1d(x_n, y_n, kind='cubic')  # интерполируем исходные нижние точки
    f2 = interp1d(x_v, y_v, kind='cubic')  # интерполируем исходные верхние точки

    x_cp = cheb_points2(7, b, a)  # х-координаты т.Чебышева на отрезке (кол-во узлов по умол. = 7)

    y_cp_bottom = f(x_cp)
    y_cp_upper = f2(x_cp)
    hc = []  # отклонение от оси х (средняя линия)
    h = []  # полувысота кажого участка на узле чебышева
    print('{:*^30}'.format('begin'))
    for i, j in zip(y_cp_upper, y_cp_bottom):
        h_t = (i - j) / 2  # полувысота кажого участка на узле чебышева
        yc_t = (j + (i - j) / 2)  # отклонение от оси х (средняя линия)
        hc.append(yc_t)
        h.append(h_t)
    x0 = x_v[0];
    print('x0 = {}'.format(x0))
    y0 = y_v[0];
    print('y0 = {}'.format(y0))
    nos = np.array([x0, y0])
    # hc.insert(0, y_v[0])  # отклонение от оси х (средняя линия) носовая точка
    hc.append(y_v[-1] - (y_v[-1] - y_n[0]) / 2)  # отклонение от оси х (средняя линия) крайняя точка
    print('hc = {}'.format(hc))

    # h.insert(0, y_v[0])  # отклонение от оси х (средняя линия) носовая точка
    h.append((y_v[-1] - y_n[0]) / 2)  # отклонение от оси х (средняя линия) крайняя точка
    print('h= {}'.format(h))

    xc = x_cp.copy()
    # xc.insert(0, x_v[0]) # носовая точка
    xc.append(x_v[-1])
    print('xc = {}'.format(xc))
    print(len(xc), len(hc), len(h))
    print('{:*^30}'.format('end'))

    plt.plot(x_n, y_n, 'y--', label=' низ.исх(y_n) ')
    plt.plot(x_v, y_v, 'm--', label=' верх.исх(y_v) ')
    plt.plot(x_cp, y_cp_bottom, 'b-', marker='.', label='BOTTOM(y_cp_bottom)')
    plt.plot(x_cp, y_cp_upper, 'r-', marker='.', label='UPPER(y_cp_upper)')
    # plt.plot(xc, h, 'c.', marker='d', label=' h')
    plt.plot(xc, hc, 'g', marker='d', label=' hc ')
    plt.grid()
    plt.minorticks_on()
    plt.legend()
    plt.show()
    print('DONE')

    mask = re.findall(shablon, filename)
    print(*mask)

    
    np.savetxt(path_target + 'xc={}.txt'.format(*mask), xc, fmt='%.4f')
    np.savetxt(path_target + 'hc={}.txt'.format(*mask), hc, fmt='%.4f')
    np.savetxt(path_target + 'h={}.txt'.format(*mask), h, fmt='%.4f')
    np.savetxt(path_target + 'nos={}.txt'.format(*mask), nos, fmt='%.4f')
