import math
import torch as t


import matplotlib.pyplot as plt 
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()


def obj_axis_aligned(xs):
    return xs[..., 0]**2 + 9*xs[..., 1]**2

def rotate(xs):
    x0 = xs[..., 0]
    x1 = xs[..., 1]
    long = (x0+x1)/math.sqrt(2)
    short = (x0-x1)/math.sqrt(2)
    return t.stack([long, short], -1)

def obj_diag(xs):
    return obj_axis_aligned(rotate(xs))

lim = 12

def contour(ax, obj):
    #Non-examinable; just for demonstration purposes.
    x0_grid, x1_grid = t.meshgrid(t.linspace(-lim, lim, 1000),
                                  t.linspace(-lim, lim, 1000),
                                  indexing="ij")

    X_grid = t.stack([x0_grid, x1_grid], dim=-1)
    f_grid = obj(X_grid)

    levels = (t.arange(8)+1)**3
    ax.contour(x0_grid, x1_grid, f_grid, linewidths=0.7, levels=levels, cmap='Greys_r', alpha=0.5)

    ax.set_xlabel("$x_1$")
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

def run(obj, opt, opt_kwargs, T=20, init=1, diag=False):
    x = t.tensor([init*(-10.), 3], requires_grad=True)
    if diag:
        rotate(x)
    xs = t.zeros(T, 2)
    xs[0] = x.data

    opt = opt((x,), **opt_kwargs)

    for i in range(1, T):
        obj(x).backward()
        opt.step()
        opt.zero_grad()
        xs[i] = x.data

    return xs


fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(6.5, 2.3))

contour(ax1, obj_axis_aligned)
xs1 = run(obj_axis_aligned, t.optim.Adam, {"lr": 2.5, "betas": (0., 0.999)})
xs2 = run(obj_axis_aligned, t.optim.Adam, {"lr": 0.5, "betas": (0., 0.999)}, init=-1)
ax1.plot(xs1[:, 0], xs1[:, 1], c='tab:blue',   label="RMSProp, lr=2.5")
ax1.plot(xs2[:, 0], xs2[:, 1], c='tab:orange', label="RMSProp, lr=0.5")

contour(ax2, obj_axis_aligned)
xs1 = run(obj_axis_aligned, t.optim.Adam, {"lr": 2.5, "betas": (0.8, 0.999)})
xs2 = run(obj_axis_aligned, t.optim.Adam, {"lr": 0.5, "betas": (0.8, 0.999)}, init=-1)
ax2.plot(xs1[:, 0], xs1[:, 1], c='tab:blue',   label="RMSProp, lr=2.5")
ax2.plot(xs2[:, 0], xs2[:, 1], c='tab:orange', label="RMSProp, lr=0.5")

contour(ax3, obj_diag)
xs1 = run(obj_diag, t.optim.Adam, {"lr": 5, "betas": (0., 0.999)})
xs2 = run(obj_diag, t.optim.Adam, {"lr": 0.5, "betas": (0., 0.999)}, init=-1)
ax3.plot(xs1[:, 0], xs1[:, 1], c='tab:blue',   label="RMSProp, lr=2.5")
ax3.plot(xs2[:, 0], xs2[:, 1], c='tab:orange', label="RMSProp, lr=0.5")

contour(ax4, obj_diag)
xs1 = run(obj_diag, t.optim.Adam, {"lr": 5, "betas": (0.8, 0.999)})
xs2 = run(obj_diag, t.optim.Adam, {"lr": 0.5, "betas": (0.8, 0.999)}, init=-1)
ax4.plot(xs1[:, 0], xs1[:, 1], c='tab:blue',   label="RMSProp, lr=2.5")
ax4.plot(xs2[:, 0], xs2[:, 1], c='tab:orange', label="RMSProp, lr=0.5")

ax1.legend(frameon=False, handletextpad=0.1, fontsize='small', borderpad=0.1, borderaxespad=0.1)

fig.savefig(args.filename, bbox_inches='tight')
