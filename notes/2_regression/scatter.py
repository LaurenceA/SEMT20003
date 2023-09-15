import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

N = 20
xs = np.linspace(-1, 1, N)
ys = 1 + 2*xs + 0.3*np.random.randn(N)
fig, axs = plt.subplots(figsize=(1.7,1.7))
axs.scatter(xs, ys, marker='.')
axs.set_xlabel('$x$')
axs.set_ylabel('$y$')

fig.savefig(args.filename, bbox_inches='tight')
