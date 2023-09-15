import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

xs = np.linspace(-6, 6, 200)
fig, axs = plt.subplots(figsize=(1.7,1.7))
axs.plot(xs, (xs > 4).astype(int) + (xs > 3.3).astype(int) + (xs > 2.1).astype(int) + (xs < -2.5).astype(int) + (xs < -4.3).astype(int) + (xs < -5.5).astype(int))
axs.set_xlabel('$w_i$')
axs.set_ylabel('$\mathcal{L}(\mathbf{w})=$ num wrong classifications')
axs.set_ylim(-0.5, 5)

fig.savefig(args.filename, bbox_inches='tight')
