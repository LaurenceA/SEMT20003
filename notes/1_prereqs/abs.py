import numpy as np
import matplotlib.pyplot as plt

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

xs = np.linspace(-1, 1, 100)
fig, axs = plt.subplots(figsize=(1.7,1.7))
axs.plot(xs, np.abs(xs))
axs.set_ylim(-1, 1)
axs.set_xlim(-1, 1)
axs.set_xlabel('x')
axs.set_ylabel('|x|')

fig.savefig(args.filename, bbox_inches='tight')
