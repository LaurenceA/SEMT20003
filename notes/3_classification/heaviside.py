import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

xs = np.linspace(-2, 2, 200)
fig, axs = plt.subplots(figsize=(1.7,1.7))
axs.plot(xs, xs > 0)
axs.set_xlabel("$a$")
axs.set_ylabel("$\Theta(a)$")
axs.set_ylim(-0.5, 1.5)

fig.savefig(args.filename, bbox_inches='tight')
