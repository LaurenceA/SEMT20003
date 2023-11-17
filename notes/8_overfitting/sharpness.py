import torch as t
import numpy as np

import matplotlib.pyplot as plt 
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.3))

lim = 3
T=20

def obj1(x):
    return 2-x.abs().rsqrt()

def obj2(x):
    return 3*x**2 - 3

def sgd(obj, init, lr=0.1):
    x = t.tensor(init, requires_grad=True)
    xs = t.zeros(T)
    ys = t.zeros(T)

    xs[0] = x.data

    for i in range(1, T):
        obj(x).backward()
        x.data = x.data - lr * x.grad
        x.grad.zero_()
        xs[i] = x.data

    return (xs, obj(xs))

ls = t.linspace(-lim, lim, 100)

ax1.set_xlim(-lim, lim)
ax1.set_ylim(-4, 2)
ax1.plot(ls, obj1(ls), c='tab:blue', alpha=0.5)
ax1.set_title("sharp minimum")
xs, objs = sgd(obj1, 1.)

for i in range(T-1):
    ax1.arrow(xs[i], objs[i], xs[i+1] - xs[i], objs[i+1] - objs[i], shape='full', length_includes_head=True, head_width=0.1, color='k')


ax2.set_xlim(-lim, lim)
ax2.set_ylim(-4, 2)
ax2.plot(ls, obj2(ls), c='tab:blue', alpha=0.5)
ax2.set_title("broad minimum")
xs, objs = sgd(obj2, 2.5)


for i in range(T-1):
    ax2.arrow(xs[i], objs[i], xs[i+1] - xs[i], objs[i+1] - objs[i], shape='full', length_includes_head=True, head_width=0.1, color='k')

ax1.set_ylabel("$\mathcal{L}$")
ax1.set_xlabel("$w$")
ax2.set_xlabel("$w$")

fig.savefig(args.filename, bbox_inches='tight')
