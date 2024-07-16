"""
Input:
    1_result_z=2.8.txt - from SCDM
Ouput:
    2_{}_for_CP_calc.txt - scaled x,y coordinates to x[0...1] to calculate Chebysevs's nodes(points)
    2_to_OptiSLang.txt - output file to OptiSLang
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import glob
import os

def sort_sym(a):
    l = list(a)
    l.sort(key=lambda p: (p[0], p[1]))

    q = deque()

    for i in range(len(l)):
        if i == 0:
            q.append(l[i])
        elif i % 2 == 0:
            q.append(l[i])
        else:
            q.appendleft(l[i])
    return np.array(q)

path = r'~'  # current path

try:
    os.mkdir(os.path.join(path, 'scdm_txt_sorted'), mode=0o777, dir_fd=None)
    print('ok')
except FileExistsError:
    print('already exists')
path_target = '~'  # 1

for filename in glob.glob('*.txt'):
    f = np.genfromtxt(filename, skip_header=True)
    print('-' * 40)
    x = f[:, 0]
    y = f[:, 1]
    plt.title(filename)
    plt.plot(x, y, 'r.-', label='origin order')
    ff = sort_sym(f)
    np.savetxt(path_target + '{}_for_Chebishev_Points.txt'.format(filename), ff, fmt='%.4f')