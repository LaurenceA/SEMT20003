import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

N = 20
xs = np.linspace(-1, 1, N)
y = 1 + 2*xs + 0.3*np.random.randn(N)
fig, axs = plt.subplots(ncols=2, figsize=(2*1.7,1.7), sharey=True)

yh = -xs
axs[0].vlines(xs, y, yh, colors='orange')
axs[0].scatter(xs, y, marker='.')
axs[0].plot(xs, yh, c='red')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_title("Bad guess")

print(np.abs(y-yh).sum())

yh = 2*xs + 1
axs[1].vlines(xs, y, yh, colors='orange')
axs[1].scatter(xs, y, marker='.')
axs[1].plot(xs, yh, c='red')
axs[1].set_xlabel('x')
axs[1].set_title("Good guess")

print(np.abs(y-yh).sum())


fig.savefig(args.filename, bbox_inches='tight')
