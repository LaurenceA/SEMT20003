import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

xs = np.linspace(-1, 1, 100)
fig, axs = plt.subplots(figsize=(1.7,1.7), sharey=True)
axs.plot(xs, xs**2)
axs.set_xlabel('$w_1$')
axs.set_ylabel('$\mathcal{L}(w_1)$')

fig.savefig(args.filename, bbox_inches='tight')
