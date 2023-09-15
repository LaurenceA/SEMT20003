import torch

import matplotlib.pyplot as plt 
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()


def obj(x):
    return x[..., 0]**2 + 9*x[..., 1]**2

lim = 12

def contour(ax, f):
    #Non-examinable; just for demonstration purposes.
    x0_grid, x1_grid = torch.meshgrid(torch.linspace(-lim, lim, 1000),
                                      torch.linspace(-lim, lim, 1000),
                                      indexing="ij")

    X_grid = torch.stack([x0_grid, x1_grid], dim=-1)
    f_grid = f(X_grid)

    levels = (torch.arange(8)+1)**3
    ax.contour(x0_grid, x1_grid, f_grid, linewidths=0.7, levels=levels, cmap='Greys_r', alpha=0.5)

def run(ax, lr, beta1):
    #Define parameters
    x_sgd = torch.tensor([-10., 3], requires_grad=True)
    v = torch.zeros(2)
    x_mom = torch.tensor([10., 3], requires_grad=True)

    #Record trajectory
    T = 15
    xs_sgd = torch.zeros(T, 2)
    xs_mom = torch.zeros(T, 2)

    #Record initial values
    xs_sgd[0] = x_sgd.data
    xs_mom[0] = x_mom.data


    #Run learning
    for t in range(1, T):
        obj(x_sgd).backward()
        x_sgd.data.add_(x_sgd.grad, alpha=-lr)
        x_sgd.grad.zero_()
        xs_sgd[t] = x_sgd.data

        obj(x_mom).backward()

        v.mul_(beta1).add_(x_mom.grad, alpha=1-beta1)
        x_mom.data.add_(v, alpha=-lr)
        x_mom.grad.zero_()
        xs_mom[t] = x_mom.data

    ax.set_xlabel("$x_1$")
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.plot(xs_sgd[:, 0], xs_sgd[:, 1], c='tab:blue',   label="SGD no momentum")
    ax.plot(xs_mom[:, 0], xs_mom[:, 1], c='tab:orange', label="SGD with momentum")

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(6.5, 2.3))

contour(ax1, obj)
contour(ax2, obj)
contour(ax3, obj)

run(ax1, lr=0.1, beta1=0.5)
run(ax2, lr=0.13, beta1=0.5)
run(ax3, lr=0.2, beta1=0.5)


ax1.set_title('$\eta_{\\rm avg} = 0.1$')
ax2.set_title('$\eta_{\\rm avg} = 0.13$')
ax3.set_title('$\eta_{\\rm avg} = 0.2$')
ax1.set_ylabel("$x_2$")
ax1.legend(frameon=False, handletextpad=0.1, fontsize='small', borderpad=0.1, borderaxespad=0.1)

fig.savefig(args.filename, bbox_inches='tight')
