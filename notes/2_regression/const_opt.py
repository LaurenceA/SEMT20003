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
fig, axs = plt.subplots(figsize=(1.7,1.7), sharey=False)
fig.tight_layout()

yh = np.mean(y)*np.ones(N)
axs.vlines(xs, y, yh, colors='orange')
axs.scatter(xs, y, marker='.')
axs.plot(xs, yh, c='red')
axs.set_xlabel('$x$')
axs.set_ylabel('$y$')
axs.set_ylim(0, 2)


fig.savefig(args.filename, bbox_inches='tight')
