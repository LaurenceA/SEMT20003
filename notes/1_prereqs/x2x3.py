import numpy as np
import matplotlib.pyplot as plt

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

xs = np.linspace(-1, 1, 100)
fig, axs = plt.subplots(ncols=3, figsize=(5,1.7), sharey=True)
axs[0].plot(xs, xs**2)
axs[1].plot(xs, -xs**2)
axs[2].plot(xs, xs**3)
for i in range(3):
    axs[i].set_xlabel('a')
axs[0].set_ylabel('L(a)')

fig.savefig(args.filename, bbox_inches='tight')
