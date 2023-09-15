import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

N = 20
xs = np.linspace(-1, 1, N)
y = 1 + 0.3*np.random.randn(N)
fig, axs = plt.subplots(ncols=2, figsize=(2*1.7,1.7), sharey=False)
fig.tight_layout()

yh = 0.9*np.ones(20)
axs[0].vlines(xs, y, yh, colors='orange')
axs[0].scatter(xs, y, marker='.')
axs[0].plot(xs, yh, c='red')
axs[0].set_xlabel('$x$')
axs[0].set_ylabel('$y$')
axs[0].set_ylim(0, 2)

w0s = np.linspace(-2, 2, 100)
Ls = np.sum((y - w0s[:, None])**2, -1)

axs[1].plot(w0s, Ls)
axs[1].set_xlabel('$w_1$')
axs[1].set_ylabel('$\\mathcal{L}(w_1)$')


fig.savefig(args.filename, bbox_inches='tight')
